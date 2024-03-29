from bson import ObjectId
from mongoengine import Document, StringField, DateTimeField, ObjectIdField, ReferenceField
from datetime import datetime


class Classes(Document):
    id: str = ObjectIdField(primary_key=True, default=ObjectId())
    name: str = StringField(required=True, min_length=3)
    code: str = StringField(required=True, min_length=2)
    description: str = StringField(required=True, min_length=5)
    parent_classe_id: str = ReferenceField("self")

    def __dict__(self):
        return {"name": self.name, "description": self.description, "code": self.code}

    # audit fields
    created: datetime = DateTimeField(default=datetime.utcnow)
    created_by = StringField(default="Epa")
    updated: datetime = DateTimeField(default=datetime.utcnow)
    meta = {"strict": False}
