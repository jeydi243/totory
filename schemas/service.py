from datetime import datetime
from mongoengine import StringField, FileField, DateTimeField, DictField, ListField
from datetime import datetime

class StudentService:
    code = StringField(required=True)
    name = StringField(required=True, min_length=20, max_length=500)
    description = StringField(min_length=6)
    website = StringField(required=False)
    contacts = ListField(DictField(required=True))
    availability = StringField(required=True)
    
    #Audit fields
    created: datetime = DateTimeField(default=datetime.now())
    created_by: str = StringField(default="user")
    updated: datetime = DateTimeField(default=datetime.now())
    updated_by: str = StringField(default="user")


