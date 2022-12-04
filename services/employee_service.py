from mongoengine import DoesNotExist
from mongoengine.errors import FieldDoesNotExist, NotUniqueError
from pydantic import ValidationError

from dtos.employee import EmployeeDTO
from schemas.employee import Employee
from schemas.organization import Organization


class EmployeeService:
    def add_employee(self, employee: EmployeeDTO, org_id=None) -> bool | str:
        try:
            emp = None
            email = self.getEmail(employee.last_name, org_id)
            if org_id != None:
                emp = Employee({**employee.dict(), org_id: org_id, email: email}).save()
            else:
                emp = Employee(**employee.dict()).save()
            print(f"Model Employee saved {emp.id}")
            return emp
        except ValidationError as ve:
            print(f"{ve.json()}")
        except TypeError as te:
            print("TypeError: ", te)
        except NotUniqueError as e:
            print(e.args[0])
        except FieldDoesNotExist as fn:
            print(f"Il te maque un champ {fn}")

    def getEmail(self, name, org_id):
        try:
            name_org = Organization.objects(id=org_id).fields(name=1)
            domain = ".org"
            return f"{name}@{name_org}{domain}"
        except BaseException as ex:
            print(ex)

    def all_employee(self) -> list[any]:
        try:
            return Employee.objects.values_list()
        except TypeError as te:
            print("TypeError: ", te)
        except ValueError as ve:
            print("ValueError: ", ve)
        except BaseException as e:
            print(f"{e}")

    def getby(self, emploeeID: str):
        return Employee.objects.get(id=emploeeID)

    def delete_employee(self, emploeeID: str):
        try:
            emp = Employee.objects.get(id=emploeeID)
            emp.delete()
            return f"Employee with ID {emploeeID} deleted."
        except DoesNotExist as e:
            print(f"Employee with ID {emploeeID}, does not exist.")

    def update_file(fieldname, fichier):
        pass

    def add_education(employeeID, education):
        Employee.objects(id=employeeID).update_one(push__educations=education)

    def update_employee(employee_id, updated_values):
        pass
