
from pydantic import ValidationException
from dtos.student_dto import StudentDTO
from schemas.student import Student
from schemas.organization import Organization
from mongoengine import DoesNotExist
from mongoengine.errors import NotUniqueError


class StudentService:
    def add_student(self, student: StudentDTO, org_id=None) -> bool | str:
        try:
            emp = Student(**student.dict()).save()
            print(f"Model Student saved {emp.id}")
            return emp
        except ValidationException as ve:
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

    def all_student(self) -> list[any]:
        try:
            if len(Student.objects) == 0:
                return []
            return Student.objects.to_json()
        except TypeError as te:
            print("TypeError: ", te)
        except ValueError as ve:
            print("ValueError: ", ve)
        except:
            print("Mais b")
        return l

    def getby(self, studentID: str):
        return Student.objects.get(id=studentID)

    def delete_student(self, studentID: str):
        try:
            emp = Student.objects.get(id=studentID)
            emp.delete()
            return f"Student with ID {studentID} deleted."
        except DoesNotExist as e:
            print(f"Student with ID {studentID}, does not exist.")

    def update_file(fieldname, fichier):
        pass

    def add_education(studentID, education):
        Student.objects(id=studentID).update_one(push__educations=education)

    def update_student(student_id, updated_values):
        pass
