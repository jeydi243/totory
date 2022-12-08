from services.gridfs_service import fs as fss, db
from fastapi import UploadFile


class ResourceService:
    def get(self, id=None) -> list[any]:
        try:
            if id is not None:
                print(f"Find file with id {id}")
                fr = fss.find_one({"_id": id})
                print(f"Voici le fichier que j'ai trouvé {fr}" if fr is not None else "Aucune entrée avec l'ID {id}")
            else:
                return fss.list()
                # for grido in fss.find():
                #     print(grido.read())
                #     grido.
        except TypeError as te:
            print("TypeError: ", te)
        except ValueError as ve:
            print("ValueError: ", ve)
        except BaseException as e:
            print(f"{e}")

    def add(self, file: UploadFile):
        try:
            print(f"Trying to pu file {file.file}")
            fss.put(file.file)

            return True
        except BaseException as e:
            print(f"Erreur lors du téléchargement {e}")
