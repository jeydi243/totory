from mongoengine import Document, EmailField, StringField, IntField, ReferenceField, DateTimeField, DictField, ListField
from person import Person
from schemas.document_organisation import DocumentOrganisation
from schemas.responsable import Responsable


class Student(Person):
    matricule: StringField(primary_key=True, min_length=10, unique=True)
    responsables: ListField(Responsable)
    status: StringField(required=True, choices=["CANDIDAT", "ETUDIANT", "DIPLOMÉ", "ABANDON", "RENVOI"])
    level: StringField(required=True, choices=["Prépa", "Bac", "Bac+1", "Bac+2", "Bac+3", "Bac+4", "Bac+5", "Bac+6"])
    highSchool: ReferenceField("HighSchool")
    documents: ListField(DocumentOrganisation)

    # init this class with all attributes
    def __init__(self, matricule, responsables, status, level, highSchool, documents):
        self.responsables = responsables
        self.matricule = matricule
        self.status = status
        self.level = level
        self.highSchool = highSchool
        self.documents = documents
        