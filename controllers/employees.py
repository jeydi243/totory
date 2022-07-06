import os
from tempfile import SpooledTemporaryFile
from dtos.employee import EmployeeDTO
from myutils import process_file
from schemas.employee import Employee
from services.employee_service import EmployeeService
from fastapi import APIRouter, Form, UploadFile, File
from shutil import copyfileobj, Error
import pathlib
from rich import print


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


@router.post("/")
def add_employee(employee):
    try:
        print({employee})
        em = employee_service.add_employee(employee)

        return {"message": "Le traitement a été fait"}
    except FileNotFoundError as ffe:
        print(f"Error: {ffe}")
        return {"message": "File not found errors"}
    except Error as er:
        print(f"Error un detected: {er}")
        return {"f": "ff"}


@router.post("/{employeeID}")
async def continue_add(
    employeeID: str, resume_file: UploadFile = File(...), school_diploma_file: UploadFile = File(...), profile_img: UploadFile = File(...)
):
    process_file(resume_file, "resume_file", employeeID, "employee")
    process_file(school_diploma_file, "school_diploma_file", employeeID, "employee")
    process_file(profile_img, "profile_img", employeeID, "employee")


@router.get("/")
def get_employees():
    return Employee.objects


@router.patch("/update/{employee_id}/{type_file}")
def update_employee(employee_id, type_file):
    result = None
    if type_file == "resume_file":
        result = employee_service.update_file("resume_file")
    elif type_file == "profile_image":
        result = employee_service.update_file("profile_image")
    else:
        result = employee_service.update_file("school_diploma_file")


@router.delete("/")
def delete_employee():
    return {"message": "Hello World"}
