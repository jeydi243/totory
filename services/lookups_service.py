import json
from rich import print
from bson import ObjectId
from typing import List
from mongoengine import Document,EmbeddedDocument,ReferenceField
from dtos.lookups_dto import LookupsDTO
from schemas.classes import Classes
from schemas.lookups import Lookups

class LookupsService:
    def add_lookups(self, lookups_dto: LookupsDTO):
        lookups_dto.classe_id = self.createClasseRef(lookups_dto.classe_id)
        co = Lookups(**lookups_dto.model_dump()).save()
        print(f"Add one lookups {co}")
        return co

    def createClasseRef(self, classe_id: str) -> Classes:
        return Classes.objects(id=classe_id)

    def getLookups(self):
        try:
            json_objects = [self.document_to_dict2(doc) for doc in Lookups.objects.select_related()]
            return json.loads(json.dumps(json_objects, default=str, indent=4))
        except BaseException as e:
            print(e)
            
    def getLookupsByClasse(self,classeID: str) -> List:
        try:
            lookups = Lookups.objects(classe_id=ObjectId(classeID)).select_related()
            json_objects = [self.document_to_dict2(doc) for doc in lookups]

            return json.loads(json.dumps(json_objects, default=str, indent=4))
        except BaseException as e:
            print(e)

    def getById(self, id: str):
        return Lookups.objects.get(id=id)
    
    def document_to_dict(self,doc):
        if isinstance(doc, Document):
            return {field: self.document_to_dict(getattr(doc, field)) for field in doc._fields}
        elif isinstance(doc, EmbeddedDocument):
            return {field: self.document_to_dict(getattr(doc, field)) for field in doc._fields}
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
                print(f'Found ObjectId for field {field}')
                data[field] = str(value)  # Convert ObjectId to string
            else:
                data[field] = value
        data['_id'] = str(doc.id)
        return data