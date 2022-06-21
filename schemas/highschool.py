from mongoengine import Document, EmailField, StringField, IntField, DateTimeField, DictField, ListField


class HighSchool(Document):
    id: StringField()
    name: StringField()
    telephones: ListField() | StringField()
    email: EmailField()
