from datetime import datetime

from mongoengine import (DateTimeField, Document, IntField, ListField,
                         ObjectIdField, ReferenceField, StringField)


class Course(Document):
    id = StringField()
    code: str = StringField(max_length=20)
    title: str = StringField(max_length=100)
    parts: list[dict] = ListField()
    authors: list[str] = ListField(required=True)
    expireDate: datetime | None = DateTimeField(default=None)
    description: str = StringField(max_length=10000)

    meta = {"strict": False}

    class Config:
        orm_mode = True
