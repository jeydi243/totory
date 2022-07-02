from datetime import datetime
from mongoengine import StringField, FileField, DateTimeField

from schemas.person import Person

class Employee(Person):
    school_start_date = StringField(required=True)
    school_end_date = StringField(required=True)
    school_diploma_file = FileField(required=True)

    cover_letter = StringField(required=True, min_length=10, max_length=1000)
    resume_file = FileField(required=True)

    profile_img = FileField(required=True)
    hire_date = DateTimeField(required=True, default=datetime.now())

    # init class
    def __init__(self, school_end_date, school_start_date):
        self.school_end_date = school_end_date
        self.school_start_date = school_start_date
        self.school_name = sc
        self.school_diploma_file = sc
