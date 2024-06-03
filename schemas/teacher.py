from mongoengine import Document, EmailField, StringField, IntField, ReferenceField, DateTimeField, DictField, ListField
from datetime import datetime
from schemas.person import Person


class Teacher(Person):
    matricule:str=  StringField(primary_key=True, min_length=7)
    resume_file:str = StringField(required=True)
    
    #Audit fields
    created: datetime = DateTimeField(default=datetime.now())
    created_by: str = StringField(default="user")
    updated: datetime = DateTimeField(default=datetime.now())
    updated_by: str = StringField(default="user")