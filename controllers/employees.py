from main import app
from mongoengine.errors import NotUniqueError
from schemas.employee import Employee
from services.employee_service import EmployeeService
from fastapi import FastAPI, Form, Request, UploadFile, File
import shutil
import os

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


app = FastAPI()
employee_service = EmployeeService()


@app.post("/management/employees")
async def add_employee(
    cover_letter: str = Form(...),
    resume_file: UploadFile = File(...),
    school_diploma_file: UploadFile = File(...),
    profile_img: UploadFile = File(...),
):

    print(resume_file.content_type)
    print(school_diploma_file.content_type)
    print(profile_img.content_type)

    try:
        path_to_store = store_path("resume_file", ext, "employees", "fd1452fvd")
        with open(path_to_store, "wb") as buffer:
            shutil.copyfileobj(resume_file.file, buffer)

        path_to_store = store_path("diploma_file", ext, "employees", "fd1452fvd")
        with open(path_to_store, "wb") as buffer:
            shutil.copyfileobj(school_diploma_file.file, buffer)

        path_to_store = store_path("profile_picture", "employees", "fd1452fvd")
        with open(path_to_store, "wb") as buffer:
            shutil.copyfileobj(profile_img.file, buffer)
    except FileNotFoundError as ffe:
        print(ffe)

    return {"message": cover_letter}


# all endpoint for model employees
@app.get("/employees")
def get_employees():
    return Employee.objects


@app.patch("/employees/update/{employee_id}/{type_file}")
def update_employee(employee_id, type_file):
    result = None
    if type_file == "resume_file":
        result = employee_service.update_file("resume_file")
    elif type_file == "profile_image":
        result = employee_service.update_file("profile_image")
    else:
        result = employee_service.update_file("school_diploma_file")


@app.delete("/employees")
def delete_employee():
    return {"message": "Hello World"}


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
