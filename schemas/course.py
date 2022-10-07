from datetime import datetime
from mongoengine import Document, EmailField, StringField, IntField, DateTimeField, ListField, ObjectIdField


class Course(Document):
    title: str = StringField(max_length=100)
    author: str = ObjectIdField(required=True)
    description: str = StringField(max_length=10000)
    expireDate: datetime | None = DateTimeField(default=None)
