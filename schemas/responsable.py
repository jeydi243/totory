from mongoengine import Document, EmailField, StringField, IntField, DateTimeField, DictField, ListField


class Responsable:
    id: StringField(required=True, min_length=7)
    name: StringField(required=True, min_length=3)
    telephones: ListField(StringField(required=True, min_length=10))
    email: EmailField(required=True)
