from mongoengine import Document, EmailField, StringField, ReferenceField, DateTimeField
import mongoengine
from datetime import datetime


class Organization(Document):
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
