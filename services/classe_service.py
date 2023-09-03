from dtos.classe_dto import ClasseDTO
from schemas.classe import Classe


class ClasseService:
    def add_classe(self, classe: ClasseDTO):
        co = Classe(**classe.dict()).save()
        print(f"add one classe {co}")
        return co

    def getClasses(self):
        try:
            val = Classe.objects.values_list()
            print(val[0].to_json())
        except BaseException as e:
            print(e)

    def getById(self, id: str):
        return Classe.objects.get(id=id)
