from typing import List
from dtos.classe_dto import ClasseDTO
from schemas.classes import Classes
from rich import print


class ClasseService:
    def add_classe(self, classe: ClasseDTO):
        print("On arrive ici c'est sure")
        co = Classes(**classe.model_dump()).save()
        print(f"Add one classe {co}")
        return co

    def getClasses(self):
        classes: List = []
        try:
            val = Classes.objects.scalar()
            print(f"Leka: {val}")
            for cl in val:
                classes.append(cl.__dict__())
            return classes
        except BaseException as e:
            print(e)

    def getById(self, id: str):
        return Classes.objects.get(id=id)
