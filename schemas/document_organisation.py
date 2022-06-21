from mongoengine import Document, EmailField, StringField, IntField, DateTimeField


class DocumentOrganisation(Document):
    code: StringField(required=True, max_length=10)
    name: StringField(required=True, max_length=50)
    description: StringField(max_length=500)
