from mongoengine import (
    Document,
    ObjectIdField,
    StringField,
    ReferenceField,
    DateTimeField,
)
import mongoengine
from bson import ObjectId
from datetime import datetime

from schemas.lookups import Lookups


class Organization(Document):
    id: str = ObjectIdField(primary_key=True, default=ObjectId())
    code: str = StringField(require=True)
    name: str = StringField(require=True)
    description: str = StringField()
    active_date: datetime = DateTimeField(default=datetime.now())
    end_date: datetime | None = DateTimeField(default=None)
    organization_parent_id: str = ReferenceField(
        "self", reverse_delete_rule=mongoengine.NULLIFY
    )
    lookup_id: str = ReferenceField(Lookups, reverse_delete_rule=mongoengine.NULLIFY)
    created: datetime = DateTimeField(default=datetime.now())
    created_by: str = StringField(default="user")
    updated: datetime = DateTimeField(default=datetime.now())
    updated_by: str = StringField(default="user")

    meta = {"strict": False}

    def __dict__(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "description": self.description,
            "code": self.code,
            "organization_parent_id": (
                str(self.organization_parent_id)
                if self.organization_parent_id
                else None
            ),
            "lookup_id": str(self.lookup_id) if self.lookup_id else None,
        }
