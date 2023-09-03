from typing import List
from dtos.lookups_dto import LookupsDTO
from schemas.lookups import Lookups
from rich import print


class LookupsService:
    def add_lookups(self, lookups_dto: LookupsDTO):
        print("On arrive ici c'est sure")
        co = Lookups(**lookups_dto.model_dump()).save()
        print(f"Add one lookups {co}")
        return co

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
