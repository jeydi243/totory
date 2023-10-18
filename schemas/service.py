from datetime import datetime
from mongoengine import StringField, FileField, DateTimeField, DictField, ListField


class StudentService:
    code = StringField(required=True)
    name = StringField(required=True, min_length=20, max_length=500)
    description = StringField(DictField(required=True))
    website = StringField(required=False)
    contacts = ListField(DictField(required=True))
    availability = StringField(required=True)


