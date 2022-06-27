from main import app
from mongoengine.errors import NotUniqueError
from schemas.student import Student
from fastapi import FastAPI, Form, Request, UploadFile, File


app = FastAPI()


@app.post("/students")
def add_student():
    try:
        res = Student().save()
    except NotUniqueError as e:
        print(e)
    return {"message": "Hello World"}


# all endpoint for model students
@app.get("/students")
def get_students():
    return Student.objects


@app.patch("/students")
def update_student():
    return {"message": "Hello World"}


@app.delete("/students")
def delete_student():
    return {"message": "Hello World"}
