from mongoengine import Document, EmailField, StringField, IntField, DateTimeField, DictField, ListField


class Classe(Document):
    id: StringField(required=True, min_length=7)
    name: StringField(required=True, min_length=3)
    description: StringField(required=True, min_length=5)
    code :StringField(required=True, min_length=2)