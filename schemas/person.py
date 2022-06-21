from mongoengine import Document, EmailField, StringField, IntField, DateTimeField


class Person(Document):
    id = StringField(primary_key=True,min_length=10)
    email = EmailField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    birthday = DateTimeField(required=True,)
