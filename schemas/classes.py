from bson import ObjectId
from mongoengine import (
    Document,
    StringField,
    DateTimeField,
    ObjectIdField,
    ReferenceField,
)
from datetime import datetime


class Classes(Document):
    id: str = ObjectIdField(primary_key=True, default=ObjectId())
    name: str = StringField(required=True, min_length=3)
    code: str = StringField(required=True, min_length=2)
    description: str = StringField(required=True, min_length=5)
    parent_classe_id: str = ReferenceField("self")

    def __dict__(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "description": self.description,
            "code": self.code,
        }

    # audit fields
    created: datetime = DateTimeField(default=datetime.now())
    created_by: str = StringField(default="user")
    updated: datetime = DateTimeField(default=datetime.now())
    updated_by: str = StringField(default="user")
    meta = {"strict": False}
