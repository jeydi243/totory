from mongoengine import Document, EmailField, StringField, IntField, ReferenceField, DateTimeField, DictField, ListField

from schemas.person import Person


class Teacher(Person):
    matricule: StringField(primary_key=True, min_length=7)
    resume_file:StringField(required=True)