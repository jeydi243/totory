from mongoengine import Document, StringField, DateTimeField
from datetime import datetime


class DocumentOrganisation(Document):
    code: str = StringField(required=True, max_length=10)
    name: str = StringField(required=True, max_length=50)
    description: str = StringField(max_length=500)

    # Audit fields
    created: datetime = DateTimeField(default=datetime.now())
    created_by: str = StringField(default="user")
    updated: datetime = DateTimeField(default=datetime.now())
    updated_by: str = StringField(default="user")
