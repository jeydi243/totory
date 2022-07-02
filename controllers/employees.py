import os
from tempfile import SpooledTemporaryFile
from dtos.employee import EmployeeDTO
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
    prefix="/management/employees",
    tags=["management"],
    responses={404: {"description": "Not found methods"}},
)

employee_service = EmployeeService()


def staff_resume(file: UploadFile):
    ext = "." + file.content_type.split("/")[1]
    path = store_path(f"resume_file{ext}",  "fd1452fvd")
    if not pathlib.Path(path).exists:
        try:
            pathlib.Path(path).mkdir(parents=True)
        except OSError as e:
            print(f"Le fichier existe déja.")
    with open(path, "wb") as buffer:
        copyfileobj(file.file, buffer)


def staff_diploma(file: UploadFile):
    ext = "." + file.content_type.split("/")[1]
    path = store_path(f"diploma_file{ext}", "fd1452fvd")
    with open(path, "wb") as buffer:
        copyfileobj(file.file, buffer)


def staff_diploma(file: UploadFile):
    ext = "." + file.content_type.split("/")[1]
    path = store_path(f"profile_picture{ext}","fd1452fvd")
    with open(path, "wb") as buffer:
        copyfileobj(file.file, buffer)


@router.post("/")
async def add_employee(
    employee: EmployeeDTO = Form(...),
    resume_file: UploadFile = File(...),
    school_diploma_file: UploadFile = File(...),
    profile_img: UploadFile = File(...),
):
    print(f"Body {employee}")

    try:
        # start by adding employee to db
        employee = employee_service.add_employee(employee)
        staff_resume(resume_file)
        staff_diploma(school_diploma_file)
        staff_resume(profile_img)

        return {"message": "Le traitement a été fait"}
    except FileNotFoundError as ffe:
        print(f"Error: {ffe}")
        return {"message": "File not found errors"}
    except Error as er:
        print(f"Error un detected: {er}")
        return {"f": "ff"}


# all endpoint for model employees
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


def store_path(filename: str, id: str) -> str:
    # return current word directory cwd
    model = "employees"
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
        print(f"{id} directory created")
    return os.path.join(to_create, filename)
