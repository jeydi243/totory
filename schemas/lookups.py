from datetime import datetime
from bson import ObjectId
from mongoengine import Document, ReferenceField, StringField, ObjectIdField,DateTimeField

from schemas.classes import Classes


class Lookups(Document):
    id: str = ObjectIdField(primary_key=True, default=ObjectId())
    name: str = StringField(max_length=200)
    code: str = StringField(max_length=20)
    description: str = StringField(max_length=100)
    classe_id: str | None = ReferenceField(Classes)
    parent_lookups_id: str | None = ReferenceField("self")
    
    #Audit fields
    created: datetime = DateTimeField(default=datetime.now())
    created_by: str = StringField(default="user")
    updated: datetime = DateTimeField(default=datetime.now())
    updated_by: str = StringField(default="user")
    
    meta = {"strict": False, "collection": "lookups"}
    
    def __dict__(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "code": self.code,
            "description": self.description,
            "parent_lookups_id": self.parent_lookups_id if self.parent_lookups_id is None else str(self.parent_lookups_id)
            # "classe_id": self.classe_id if self.classe_id is None else str(self.classe_id),
        }

    class Config:
        from_attributes = False
