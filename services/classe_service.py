from typing import List

from bson import ObjectId
from dtos.classe_dto import ClasseDTO
from schemas.classes import Classes
from rich import print
import json

class ClasseService:
    def add_classe(self, classe: ClasseDTO):
        print("On arrive ici c'est sure")
        co = Classes(**classe.model_dump()).save()
        print(f"Add one classe {co}")
        return co

    def getClasses(self):
        try:
            json_strings = [doc.to_json() for doc in Classes.objects()]
            json_objects = [json.loads(json_str) for json_str in json_strings]
            return json_objects
        except BaseException as e:
            print(e)

    def getClasseByID(self, ID: str):
        return Classes.objects.get(id=ObjectId(ID))
