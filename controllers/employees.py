from main import app
from mongoengine.errors import NotUniqueError
from schemas.employee import Employee
from fastapi import FastAPI, Form, Request, UploadFile, File


app = FastAPI()


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


@app.patch("/employees")
def update_employee():
    return {"message": "Hello World"}


@app.delete("/employees")
def delete_employee():
    return {"message": "Hello World"}
