from enum import unique
from mongoengine import Document, EmailField, StringField, IntField, DateTimeField, ListField
from datetime import datetime

class Person(Document):
    personal_email = EmailField(required=True, unique=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    middle_name = StringField(required=True)

    gender = StringField(required=True)
    email = StringField()
    telephones = ListField(StringField(required=True))
    address = StringField(required=True)
    birthday = StringField(required=True)

    meta = {"abstract": True, "strict": False}
