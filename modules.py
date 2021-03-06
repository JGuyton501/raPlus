from app import *
from datetime import datetime
# registering users into database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    pw_hash = db.Column(db.String(250))
    position = db.Column(db.String(80))
    floor = db.Column(db.String(3))
    res_college = db.Column(db.String(3))
    def __init__(
        self,
        first_name,
        last_name,
        email,
        password,
        position,
        floor,
        res_college
    ):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.position = position
        self.floor = floor
        self.res_college = res_college
        #UserMixin.__init__(self,roles)

    def __repr__(self):
        return '<Name %r>' % self.email
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

 # adding programs
 # change the types later
class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    program_name = db.Column(db.String(80))
    program_type = db.Column(db.String(80))
    date = db.Column(db.DateTime)
    time = db.Column(db.String(10))
    location = db.Column(db.String(80))
    description = db.Column(db.String(500))
    owner_first_name = db.Column(db.String(80))
    owner_last_name = db.Column(db.String(80))
    organizations_involved = db.Column(db.String(50))
    community = db.Column(db.String(50))
    money_spent = db.Column(db.String(30))
    implementation = db.Column(db.String(500))
    improvement = db.Column(db.String(500))
    assessment = db.Column(db.String(500))


    def __init__(
        self,
        program_name,
        program_type,
        date,
        time,
        location,
        description,
        owner_first_name,
        owner_last_name,
        organizations_involved,
        community,
        money_spent,
        implementation,
        improvement,
        assessment
    ):

        self.program_name = program_name
        self.program_type = program_type
        self.date = date
        self.time = time
        self.location = location
        self.description = description
        self.owner_first_name = owner_first_name
        self.owner_last_name = owner_last_name
        self.organizations_involved = organizations_involved
        self.community = community
        self.money_spent = money_spent
        self.implementation = implementation
        self.improvement = improvement
        self.assessment = assessment

    def __repr__(self):
        return '<Program Name %r>' % self.program_name

# resident 1:1
class one_on_one(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resident_first_name = db.Column(db.String(80))
    resident_last_name = db.Column(db.String(80))
    room_number = db.Column(db.String(10))
    date = db.Column(db.DateTime)
    notes = db.Column(db.String(1000))
    floor = db.Column(db.String(3))
    res_college = db.Column(db.String(3))

    def __init__(
        self,
        resident_first_name,
        resident_last_name,
        room_number,
        date,
        notes,
        floor,
        res_college
    ):

        self.resident_first_name = resident_first_name
        self.resident_last_name = resident_last_name
        self.room_number = room_number
        self.date = date
        self.notes = notes
        self.floor = floor
        self.res_college = res_college

    def __repr__(self):
        return '<Name %r>' % self.resident_first_name

# ra directory
class ra_directory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_first_name = db.Column(db.String(80))
    staff_last_name = db.Column(db.String(80))
    room_number = db.Column(db.String(80))
    residential_community = db.Column(db.String(50))
    residential_building = db.Column(db.String(50))
    cell_phone = db.Column(db.String(15))
    home_location = db.Column(db.String(40))
    birth_date = db.Column(db.String(20))
    school = db.Column(db.String(40))
    status = db.Column(db.String(20))
    email = db.Column(db.String(100))
    profile_image = db.Column(db.String(170))

    def __init__(
        self,
        staff_first_name,
        staff_last_name,
        room_number,
        residential_community,
        residential_building,
        cell_phone,
        home_location,
        birth_date,
        school,
        status,
        email,
        profile_image
    ):

        self.staff_first_name = staff_first_name
        self.staff_last_name = staff_last_name
        self.room_number = room_number
        self.residential_community = residential_community
        self.residential_building = residential_building
        self.cell_phone = cell_phone
        self.home_location = home_location
        self.birth_date = birth_date
        self.school = school
        self.status = status
        self.email = email
        self.profile_image = profile_image

    def __repr__(self):
        return '<Name %r>' % self.staff_first_name

# resident directory
class resident_directory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resident_first_name = db.Column(db.String(80))
    resident_last_name = db.Column(db.String(80))
    room_number = db.Column(db.String(80))
    residential_building = db.Column(db.String(50))
    sub_free = db.Column(db.String(5))
    cell_phone = db.Column(db.String(15))
    home_location = db.Column(db.String(40))
    birth_date = db.Column(db.String(20))
    school = db.Column(db.String(40))
    status = db.Column(db.String(20))
    email = db.Column(db.String(100))
    profile_image = db.Column(db.String(170))

    def __init__(
        self,
        resident_first_name,
        resident_last_name,
        room_number,
        residential_building,
        sub_free,
        cell_phone,
        home_location,
        birth_date,
        school,
        status,
        email,
        profile_image
    ):

        self.resident_first_name = resident_first_name
        self.resident_last_name = resident_last_name
        self.room_number = room_number
        self.residential_building = residential_building
        self.sub_free = sub_free
        self.cell_phone = cell_phone
        self.home_location = home_location
        self.birth_date = birth_date
        self.school = school
        self.status = status
        self.email = email
        self.profile_image = profile_image

    def __repr__(self):
        return '<Name %r>' % self.staff_first_name
