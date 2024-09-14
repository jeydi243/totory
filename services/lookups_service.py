import json
from re import A
from rich import print
from bson import ObjectId
from typing import List
from mongoengine import Document, EmbeddedDocument, ReferenceField
from fastapi.exceptions import ValidationException
from dtos.lookups_dto import LookupsDTO
from schemas.classes import Classes
from schemas.lookups import Lookups


class LookupsService:
    def add_lookups(self, lookups_dto: LookupsDTO) -> dict | LookupsDTO:
        try:
            if lookups_dto.classe_id != None:
                lookups_dto.classe_id = self.createClasseRef(lookups_dto.classe_id)[0]
            else:
                return {"erreur": "Il faut definir la classe du lookups"}
            # print(**lookups_dto.model_dump_json(exclude_none=True))
            # co = Lookups(**lookups_dto.model_dump()).save()
            co = Lookups(**dict(lookups_dto)).save()
            # print(f"Added one lookups = {co}")
            return co
        except BaseException as e:
            print(e)

    def updateLookups(self, lookupsUpdate: LookupsDTO):
        try:
            print(f'Update lookup with ID={lookupsUpdate.id}')
            lookups_found = Lookups.objects.get(id=ObjectId(lookupsUpdate.id))
            for key, value in dict(lookupsUpdate).items():
                if key != 'classe_id':
                    lookups_found[key] = value
                    print(f"Update key={key} by value='{value}'")
                    
                elif key == 'classe_id' and self.is_valid_objectid(value) == True:
                    lookups_found[key] = value
                    
            lookups_found.save()
            
        except ValidationException as e:
            print(f"An ValidationException occurred {e} ")    
        except BaseException as e:
            print(f"An exception occurred {e} ")
        
    def is_valid_objectid(objectid_str):
        try:
            ObjectId(objectid_str)
            return True
        except Exception:
            return False
        
    def createClasseRef(self, classe_id: str) -> Classes:
        return Classes.objects(id=classe_id)

    def getLookups(self):
        try:
            json_objects = [
                self.document_to_dict2(doc) for doc in Lookups.objects.select_related()
            ]
            return json.loads(json.dumps(json_objects, default=str, indent=4))
        except BaseException as e:
            print(e)

    def getLookupsByClasse(self, classeID: str) -> List:
        try:
            lookups = Lookups.objects(classe_id=ObjectId(classeID)).select_related()
            json_objects = [self.document_to_dict2(doc) for doc in lookups]

            return json.loads(json.dumps(json_objects, default=str, indent=4))
        except BaseException as e:
            print(e)

    def getById(self, id: str):
        return Lookups.objects.get(id=ObjectId(id))

    def deleteOneLookups(self, id: str):
        deleteLookups = Lookups.objects.get(id=ObjectId(id))
        deleteLookups.delete()
        return {"ok": "Le document est supprimé avec succès. "}

    def document_to_dict(self, doc):
        if isinstance(doc, Document):
            return {
                field: self.document_to_dict(getattr(doc, field))
                for field in doc._fields
            }
        elif isinstance(doc, EmbeddedDocument):
            return {
                field: self.document_to_dict(getattr(doc, field))
                for field in doc._fields
            }
        elif isinstance(doc, ReferenceField):
            return self.document_to_dict(doc.to_mongo())
        elif isinstance(doc, (list, tuple)):
            return [self.document_to_dict(item) for item in doc]
        else:
            return doc

    def document_to_dict2(self, doc):
        """Convert MongoEngine document to dictionary, including referenced documents."""
        data = {}
        for field in doc._fields:
            value = getattr(doc, field)
            if isinstance(doc._fields[field], ReferenceField):
                data[field] = self.document_to_dict2(value) if value else None
            elif isinstance(value, ObjectId):
                data[field] = str(value)  # Convert ObjectId to string
            else:
                data[field] = value
        data["_id"] = str(doc.id)
        return data


