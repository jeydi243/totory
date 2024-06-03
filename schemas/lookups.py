from datetime import datetime
from bson import ObjectId
from mongoengine import Document, ReferenceField, StringField, ObjectIdField,DateTimeField


class Lookups(Document):
    id: str = ObjectIdField(primary_key=True, default=ObjectId())
    code: str = StringField(max_length=20)
    description: str = StringField(max_length=100)
    classe_id: str = ReferenceField("Classes")
    
    #Audit fields
    created: datetime = DateTimeField(default=datetime.now())
    created_by: str = StringField(default="user")
    updated: datetime = DateTimeField(default=datetime.now())
    updated_by: str = StringField(default="user")
    
    meta = {"strict": False, "collection": "lookups"}
    
    def __dict__(self):
        return {
            "id": str(self.id),
            "code": self.code,
            "description": self.description,
            "classe_id": self.classe_id,
        }

    class Config:
        from_attributes = False
