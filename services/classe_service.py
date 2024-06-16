from typing import List

from bson import ObjectId
from dtos.classe_dto import ClasseDTO
from schemas.classes import Classes
from rich import print
import json
from mongoengine import Document, ReferenceField


class ClasseService:
    def add_classe(self, classe: ClasseDTO):
        print("On arrive ici c'est sure")
        co = Classes(**classe.model_dump()).save()
        print(f"Add one classe {co}")
        return co

    def getClasses(self):
        try:
            json_strings = [doc.to_json() for doc in Classes.objects()]
            json_test = [doc.__dict__() for doc in Classes.objects()]
            print(f"Ici = {json_test}")
            return json_test
            # json_objects = [json.loads(json_str) for json_str in json_strings]
            # return json_objects
        except BaseException as e:
            print(e)
            
    def getCountClasses(self) -> int:
        try:
            return Classes.objects.count()
        except BaseException as e:
            print(e)

    def getClasseByID(self, ID: str):
        return Classes.objects.get(id=ObjectId(ID))

    def document_to_dict2(self, doc):
        """Convert MongoEngine document to dictionary, including referenced documents."""
        data = {}
        for field in doc._fields:
            value = getattr(doc, field)
            if isinstance(doc._fields[field], ReferenceField):
                data[field] = self.document_to_dict2(value) if value else None
            elif isinstance(value, ObjectId):
                print(f"Found ObjectId for field {field}")
                data[field] = str(value)  # Convert ObjectId to string
            else:
                data[field] = value
        data["_id"] = str(doc.id)
        return data
