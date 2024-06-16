from mongoengine import Document, ObjectIdField, StringField, ReferenceField, DateTimeField
import mongoengine
from bson import ObjectId
from datetime import datetime


class Organization(Document):
    id: str = ObjectIdField(primary_key=True, default=ObjectId())
    code: str = StringField(require=True)
    name: str = StringField(require=True)
    description: str = StringField()
    organization_parent_id: str = ReferenceField(
        "self", reverse_delete_rule=mongoengine.NULLIFY
    )
    created: datetime = DateTimeField(default=datetime.now())
    created_by: str = StringField(default="user")
    updated: datetime = DateTimeField(default=datetime.now())
    updated_by: str = StringField(default="user")

    meta = {"strict": False}
