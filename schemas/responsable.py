from mongoengine import (
    Document,
    EmailField,
    StringField,
    IntField,
    DateTimeField,
    DictField,
    ListField,
)
from datetime import datetime


class Responsable:
    id: str = StringField(required=True, min_length=7)
    name: str = StringField(required=True, min_length=3)
    telephones: str = ListField(StringField(required=True, min_length=10))
    email: str = EmailField(required=True)
    
    #Audit fields
    created: datetime = DateTimeField(default=datetime.now())
    created_by: str = StringField(default="user")
    updated: datetime = DateTimeField(default=datetime.now())
    updated_by: str = StringField(default="user")
