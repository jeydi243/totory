from pydantic import ValidationError
from dtos.employee import EmployeeDTO
from schemas.employee import Employee


class EmployeeService:
    def add_employee(employee: EmployeeDTO) -> bool | str:
        try:
            employee = Employee(employee).save()
            return employee
        except ValidationError as ve:
            print(f"Something went wrong {ve.json()}")

    def all_employee():
        return Employee.objects

    def update_file(fieldname, fichier):
        pass

    def update_employee(employee_id, updated_values):
        pass
