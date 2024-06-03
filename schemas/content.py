from datetime import datetime

from bson import ObjectId
from mongoengine import (
    DateTimeField,
    Document,
    IntField,
    ListField,
    ObjectIdField,
    ReferenceField,
    StringField,
)


class Content(Document):
    id = ObjectIdField(primary_key=True, default=ObjectId())
    code: str = StringField(max_length=20)
    title: str = StringField(max_length=100)
    parts: list[dict] = ListField()
    authors: list[str] = ListField(required=True)
    expireDate: datetime | None = DateTimeField(default=None)
    description: str = StringField(max_length=10000)
    
    #Audit fields
    created: datetime = DateTimeField(default=datetime.now())
    created_by: str = StringField(default="user")
    updated: datetime = DateTimeField(default=datetime.now())
    updated_by: str = StringField(default="user")

    meta = {"strict": False}

    class Config:
        from_attributes = True
