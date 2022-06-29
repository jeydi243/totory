from main import app
from mongoengine.errors import NotUniqueError
from schemas.employee import Employee
from services.employee_service import EmployeeService
from fastapi import FastAPI, Form, Request, UploadFile, File


app = FastAPI()
employee_service = EmployeeService



@app.post("/employees")
def add_employee():
    try:
        res = Employee().save()
    except NotUniqueError as e:
        print(e)
    return {"message": "Hello World"}


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
