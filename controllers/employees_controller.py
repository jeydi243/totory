import os
from shutil import Error

from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import Response
from fastapi.exceptions import RequestValidationError, ValidationError
from rich import print

from dtos.education_dto import EducationDTO
from dtos.employee_dto import EmployeeDTO
from myutils import process_file
from schemas.employee import Employee
from services.employee_service import EmployeeService


def store_path(filename: str, ext: str, model: str, id: str) -> str:
    # return current word directory cwd
    to_create = os.path.join(os.getcwd(), "STORAGES")
    if not os.path.exists(to_create):
        os.mkdir(to_create)
        print("STORAGES directory created")
        to_create = os.path.join(to_create, model.upper())
    if not os.path.exists(to_create):
        os.mkdir(to_create)
        print(f"{model.upper()} directory created")
        to_create = os.path.join(to_create, id)
    if not os.path.exists(to_create):
        os.mkdir(to_create)
    return os.path.join(to_create, filename)


router = APIRouter(
    prefix="/employees",
    tags=["management"],
    responses={404: {"description": "Not found methods"}},
)

employee_service = EmployeeService()


@router.get("")
def get_employees():
    print("To get all employees")
    return employee_service.all_employee()


@router.post("")
def add_employee(employeeDTO: EmployeeDTO):
    try:
        print(employeeDTO.dict())
        employee_created = employee_service.add_employee(employeeDTO)
        print(f"{employee_created=}")
        return employee_created
    except ValidationError as e:
        print(f"ValidationException:{e.json()}")
    except BaseException as er:
        print(f"BaseException: {er}")
        return Response(status_code=400, content={"message": "Impossible de hacher le DTO"})


@router.post("{employee_id}/add_education")
def add_education(employee_id: str, education: EducationDTO):
    employee_service.add_education(employee_id, education)
    pass


@router.post("{employee_id}/add_experience")
def add_experience():
    print("Hey...")
    pass


@router.post("{employee_id}/update_biography")
def add_experience():
    print("Hey...")
    pass


@router.post("/{employeeID}")
async def continue_add(employeeID: str, resume_file: UploadFile = File(...), school_diploma_file: UploadFile = File(...), profile_img: UploadFile = File(...)):
    process_file(resume_file, "resume_file", employeeID, "employee")
    process_file(school_diploma_file, "school_diploma_file", employeeID, "employee")
    process_file(profile_img, "profile_img", employeeID, "employee")


@router.get("/{emploeeID}")
def employeeBy(emploeeID: str):
    return employee_service.getby(emploeeID)


@router.patch("/update/{employee_id}/{type_file}")
def update_employee(employee_id, type_file):
    result = None
    if type_file == "resume_file":
        result = employee_service.update_file("resume_file")
    elif type_file == "profile_image":
        result = employee_service.update_file("profile_image")
    else:
        result = employee_service.update_file("school_diploma_file")


@router.delete("/{employeeID}")
def delete_employee(employeeID: str):
    return employee_service.delete_employee(employeeID)
