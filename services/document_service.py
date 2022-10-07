from pydantic import ValidationError
from mongoengine import DoesNotExist
from dtos.documentDTO import DocumentDTO
from dtos.employee import EmployeeDTO
from schemas.document_organisation import DocumentOrganisation
from mongoengine.errors import NotUniqueError, FieldDoesNotExist
from schemas.organization import Organization
from schemas.document_organisation import DocumentOrganisation


class DocumentService:
    def add(self, newdoc: DocumentDTO) -> bool | dict:
        try:
            print(f"Epll: {newdoc.dict()}")
            doc = DocumentOrganisation(**newdoc.dict()).save()
            print(f"Model DocumentOrganisation saved with {doc.id=}")
            return doc
        except ValidationError as ve:
            print(f"{ve.json()}")
        except TypeError as te:
            print("TypeError: ", te)
        except NotUniqueError as e:
            print(e.args[0])
        except FieldDoesNotExist as fn:
            print(fn)

    def deleteBy(self):
        pass

    def getDocuments(self) -> list[any]:
        try:
            vr = DocumentOrganisation.objects.as_pymongo()
            for item in vr:
                # print(f"Le monde {dir(item)}")
                print(f"Le  {item}")
            return DocumentOrganisation.objects(__raw__={})
        except TypeError as te:
            print("TypeError: ", te)
        except ValueError as ve:
            print("ValueError: ", ve)
        except BaseException as e:
            print(f"{e}")

    def update(self):
        pass
