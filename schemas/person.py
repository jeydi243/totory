from enum import unique
from mongoengine import (
    Document,
    EmailField,
    StringField,
    ObjectIdField,
    DateTimeField,
    ListField,
)
from datetime import datetime
from bson import ObjectId


class Person(Document):
    id: str = ObjectIdField(primary_key=True, default=ObjectId())
    personal_email: str = EmailField(required=True, unique=True)
    first_name: str = StringField(required=True)
    last_name: str = StringField(required=True)
    middle_name: str = StringField(required=True)

    gender: str = StringField(required=True)
    email: str = StringField()
    telephones: str = ListField(StringField(required=True))
    address: str = StringField(required=True)
    birthday: str = StringField(required=True)

    meta = {"abstract": True, "strict": False}
