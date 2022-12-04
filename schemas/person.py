from enum import unique
from mongoengine.queryset import queryset_manager
from mongoengine import Document, EmailField, StringField, IntField, DateTimeField, ListField, ObjectIdField
from bson.objectid import ObjectId


class Person(Document):
    id = ObjectIdField(primary_key=True, default=ObjectId())

    personal_email = EmailField(required=True, unique=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    middle_name = StringField(required=True)

    gender = StringField(required=True)
    email = EmailField()
    telephones = ListField(StringField(required=True))
    address = StringField(required=True)
    birthday = StringField(required=True)
    
    @queryset_manager
    def live_posts(doc_cls, queryset):
        return doc_cls.id

    meta = {"abstract": True, "strict": False}
