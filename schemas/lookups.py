from datetime import datetime

from mongoengine import (DateTimeField, Document, IntField, ListField,
                         ObjectIdField, ReferenceField, StringField)


class Lookups(Document):
    id = StringField()
    code: str = StringField(max_length=20)
    description: str = StringField(max_length=100)
    classe_id: str = ReferenceField('Classe',dbref=False)

    meta = {"strict": False}

    class Config:
        orm_mode = True
