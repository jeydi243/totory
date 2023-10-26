from pydantic import ValidationError
from dtos.service_dto import ServiceDTO
from schemas.service import StudentService
from schemas.organization import Organization
from mongoengine import DoesNotExist
from mongoengine.errors import NotUniqueError


class SService:
    def add_service(self, service: ServiceDTO, org_id=None) -> bool | str:
        try:
            emp = StudentService(**service.dict()).save()
            print(f"Model Service saved {emp.id}")
            return emp
        except ValidationError as ve:
            print(f"{ve.json()}")
        except TypeError as te:
            print("TypeError: ", te)
        except NotUniqueError as e:
            print(e.args[0])

    def all_service(self) -> list[any]:
        l: [] = []
        try:
            if len(StudentService.objects) == 0:
                return l
            return StudentService.objects.to_json()
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

    def updateFile(self,serviceID, file):
        serv = StudentService.objects(id=serviceID).update_one(set__img=file)
        serv.img.replace(file)
        serv.save()

    def add_education(self,serviceID, education):
        StudentService.objects(id=serviceID).update_one(push__educations=education)
        
    def add_skills(self,serviceID, skill):
        StudentService.objects(id=serviceID).update_one(push__skills=skill)

    def update_service(self,serviceID, updated_values):
        pass
