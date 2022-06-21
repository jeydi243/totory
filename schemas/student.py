from mongoengine import Document, EmailField, StringField, IntField, ReferenceField, DateTimeField, DictField, ListField
from person import Person
from schemas.document_organisation import DocumentOrganisation
from schemas.responsable import Responsable


class Student(Person):
    matricule: StringField(primary_key=True, min_length=10)
    responsables: ListField(Responsable)
    status: StringField(required=True, choices=["active", "inactive"])
    level: StringField(required=True, choices=["junior", "senior"])
    highSchool: ReferenceField("HighSchool")
    documents: ListField(DocumentOrganisation)
