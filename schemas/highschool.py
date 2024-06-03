from typing import List
from mongoengine import Document, EmailField, StringField, DateTimeField, ListField
from datetime import datetime

class HighSchool(Document):
    id: str = StringField()
    name: str =StringField()
    telephones:str | List = ListField() | StringField()
    email: str = EmailField()
    created: datetime = DateTimeField(default=datetime.now())
    created_by: str = StringField(default="user")
    updated: datetime = DateTimeField(default=datetime.now())
    updated_by: str = StringField(default="user")
