




from lib2to3.pytree import Base
from pydantic import ValidationError
from dtos.teacher import TeacherDTO
from schemas.teacher import Teacher
from schemas.organization import Organization
from mongoengine import DoesNotExist
from mongoengine.errors import NotUniqueError


class TeacherService:
    def add_teacher(self, teacher: TeacherDTO, org_id=None) -> bool | str:
        try:
            emp = Teacher(**teacher.dict()).save()
            print(f"Model Teacher saved {emp.id}")
            return emp
        except ValidationError as ve:
            print(f"{ve.json()}")
        except TypeError as te:
            print("TypeError: ", te)
        except NotUniqueError as e:
            print(e.args[0])

    def getEmail(self, name, org_id):
        try:
            name_org = Organization.objects(id=org_id).fields(name=1)
            domain = ".org"
            return f"{name}@{name_org}{domain}"
        except BaseException as ex:
            print(ex)

    def all_teacher(self) -> list[any]:
        try:
            if len(Teacher.objects) == 0:
                return []
            return Teacher.objects.to_json()
        except TypeError as te:
            print("TypeError: ", te)
        except ValueError as ve:
            print("ValueError: ", ve)
        except:
            print("Mais b")
        return l

    def getby(self, emploeeID: str):
        return Teacher.objects.get(id=emploeeID)

    def delete_teacher(self, teacherID: str):
        try:
            emp = Teacher.objects.get(id=emploeeID)
            emp.delete()
            return f"Teacher with ID {emploeeID} deleted."
        except DoesNotExist as e:
            print(f"Teacher with ID {emploeeID}, does not exist.")

    def update_file(fieldname, fichier):
        pass

    def add_education(teacherID, education):
        Teacher.objects(id=teacherID).update_one(push__educations=education)

    def update_teacher(teacher_id, updated_values):
        pass
