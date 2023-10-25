
from pydantic import ValidationError
from dtos.service_dto import ServiceDTO
from schemas.service import StudentService
from schemas.organization import Organization
from mongoengine import DoesNotExist
from mongoengine.errors import NotUniqueError


class Service:
    def add_service(self, service: ServiceDTO, org_id=None) -> bool | str:
        try:
            emp = Service(**service.dict()).save()
            print(f"Model Service saved {emp.id}")
            return emp
        except ValidationError as ve:
            print(f"{ve.json()}")
        except TypeError as te:
            print("TypeError: ", te)
        except NotUniqueError as e:
            print(e.args[0])

    def all_service(self) -> list[any]:
        l:[] = []
        try:
            if len(Service.objects) == 0:
                return l
            return Service.objects.to_json()
        except TypeError as te:
            print("TypeError: ", te)
        except ValueError as ve:
            print("ValueError: ", ve)
        except:
            print("Mais b")
        return l

    def getby(self, serviceID: str):
        return Service.objects.get(id=serviceID)

    def delete_service(self, serviceID: str):
        try:
            emp = Service.objects.get(id=serviceID)
            emp.delete()
            return f"Service with ID {serviceID} deleted."
        except DoesNotExist as e:
            print(f"Service with ID {serviceID}, does not exist.")

    def update_file(fieldname, fichier):
        pass

    def add_education(serviceID, education):
        Service.objects(id=serviceID).update_one(push__educations=education)

    def update_service(service_id, updated_values):
        pass
