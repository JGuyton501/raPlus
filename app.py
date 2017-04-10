from __future__ import print_function
import os,sys
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user,current_user
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)
app.secret_key = "foobarbazz"
app.debug = True

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/raPlus'

#import modules after init app
db = SQLAlchemy(app)
import modules

@app.route('/')
def login():
    return render_template('main/login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('user/dashboard.html')

@app.route('/features')
def features():
    return render_template('main/features.html')

@app.route('/signup')
def signup():
    return render_template('main/signup.html')

# @app.route('/login')
# def login():
#     return render_template('main/login.html')

@app.route('/submit_program')
def submit():
    return render_template('user/submit_program.html')

@app.route('/submit_1-1')
def submit1():
    return render_template('user/submit_1-1.html')

@app.route('/calendar')
def calendar():
    return render_template('user/calendar.html')


# modules below
# post new user
@app.route('/post_user', methods=['POST'])
def post_user():
    user = modules.User(
        request.form['first_name'],
        request.form['last_name'],
        request.form['email'],
        request.form['password']
        )
    user.set_password(user.password)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('home'))

# post one on one
@app.route('/submit_1-1', methods=['POST'])
def post_1():
    resident1 = modules.OneonOne(
        request.form['resident_first_name'],
        request.form['resident_last_name'],
        request.form['housing'],
        request.form['room_number'],
        request.form['recommended_resources'],
        request.form['concerns'],
        request.form['notes']
        )
    db.session.add(resident1)
    db.session.commit()
    return redirect(url_for('home'))

# post new program
@app.route('/post_program', methods=['POST'])
def post_program():
    program = modules.Program(
        request.form['program_name'],
        request.form['program_type'],
        request.form['date'],
        request.form['time'],
        request.form['location'],
        request.form['primary_sponsor'],
        request.form['secondary_sponsor'],
        request.form['community'],
        request.form['organizations_involved'],
        request.form['money_spent'],
        request.form['description'],
        request.form['implementation'],
        request.form['improvement'],
        request.form['assessment']
        )
    db.session.add(program)
    db.session.commit()
    return redirect(url_for('home'))

# query programs
@app.route('/programs')
def programs():
    allPrograms = modules.Program.query.all()
    return render_template('user/programs_list.html', allPrograms = allPrograms)

# query OneonOnes
@app.route('/OneonOne')
def OneonOne():
    OneonOneList = modules.Program.query.all()
    return render_template('user/oneonone_list.html', OneonOneList = OneonOneList)

# query ra directory 
@app.route('/ra-directory')
def ra_directory():
    allRA = modules.ra_directory.query.all()
    return render_template('user/ra_directory.html', allRA = allRA)


@app.route('/post_login', methods=['POST'])
def post_login():
    form_email = request.form['email']
    form_pass = request.form['password']
    user = modules.User.query.filter_by(email=form_email).first()
    if user is None:
        print("No user with this email")
    elif user.check_password(form_pass):
        print(user.first_name + ' Logged in successfully.',file=sys.stderr)
        login_user(user)
    else:
        print("Invalid password")
    return redirect(url_for('home'))

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return modules.User.query.get(int(user_id))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "You have been logged out"

@app.route('/hummus')
@login_required
def hummus():
    return "The current user is" + current_user.last_name

@app.route('/test_log')
def test_log():
    x = 'jessehuang@wustl.edu'
    user = modules.User.query.filter_by(email=x).first()
    print(user.first_name, file=sys.stderr)
    login_user(user)
    return user.last_name + " Was logged in"


if __name__ == '__main__':
    app.run()
