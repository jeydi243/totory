from dtos.classe_dto import ClasseDTO
from schemas.classes import Classes
from rich import print


class ClasseService:
    def add_classe(self, classe: ClasseDTO):
        print("On arrive ici c'est sure")
        co = Classes(**classe.model_dump()).save()     
        print(f"add one classe {co}")
        return co

    def getClasses(self):
        try:
            val = Classes.objects.values_list()
            print(val[0].to_json())
        except BaseException as e:
            print(e)

    def getById(self, id: str):
        return Classes.objects.get(id=id)
