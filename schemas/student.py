from mongoengine import (
    StringField,
    ReferenceField,
    DateTimeField,
    ListField,
)
from schemas.person import Person
from schemas.document_organisation import DocumentOrganisation
from schemas.responsable import Responsable
from datetime import datetime


class Student(Person):
    matricule: str = StringField(min_length=10, unique=True)
    responsables: str = ListField(Responsable)
    status: str = StringField(
        required=True, choices=["CANDIDAT", "ETUDIANT", "DIPLOMÉ", "ABANDON", "RENVOI"]
    )
    level: str = StringField(
        required=True,
        choices=["Prépa", "Bac", "Bac+1", "Bac+2", "Bac+3", "Bac+4", "Bac+5", "Bac+6"],
    )
    highSchool: str = ReferenceField("HighSchool")
    documents: str = ListField(DocumentOrganisation)

    # Audit fields
    created: datetime = DateTimeField(default=datetime.now())
    created_by: str = StringField(default="user")
    updated: datetime = DateTimeField(default=datetime.now())
    updated_by: str = StringField(default="user")

    # init this class with all attributes
    def __init__(self, matricule, responsables, status, level, highSchool, documents):
        self.responsables = responsables
        self.matricule = matricule
        self.status = status
        self.level = level
        self.highSchool = highSchool
        self.documents = documents
