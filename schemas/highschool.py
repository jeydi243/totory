from typing import List
from mongoengine import (
    Document,
    EmailField,
    StringField,
    DateTimeField,
    ListField,
    ObjectIdField,
)
from datetime import datetime
from bson import ObjectId


class HighSchool(Document):
    id: str = ObjectIdField(primary_key=True, default=ObjectId())
    name: str = StringField()
    telephones: str | List = ListField() | StringField()
    email: str = EmailField()

    # audit fields
    created: datetime = DateTimeField(default=datetime.now())
    created_by: str = StringField(default="user")
    updated: datetime = DateTimeField(default=datetime.now())
    updated_by: str = StringField(default="user")
