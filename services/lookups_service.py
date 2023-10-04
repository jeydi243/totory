from typing import List
from dtos.lookups_dto import LookupsDTO
from schemas.classes import Classes
from schemas.lookups import Lookups
from rich import print


class LookupsService:
    def add_lookups(self, lookups_dto: LookupsDTO):
        lookups_dto.classe_id = self.createClasseRef(lookups_dto.classe_id)
        co = Lookups(**lookups_dto.model_dump()).save()
        print(f"Add one lookups {co}")
        return co

    def createClasseRef(self, classe_id: str) -> Classes:
        return Classes.objects(id=classe_id)

    def getLookups(self):
        lookups: List = []
        try:
            val = Lookups.objects.scalar()
            print(f"Leka: {val}")
            for cl in val:
                lookups.append(cl.__dict__())
            return lookups
        except BaseException as e:
            print(e)

    def getById(self, id: str):
        return Lookups.objects.get(id=id)
