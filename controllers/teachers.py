from main import app
from mongoengine.errors import NotUniqueError
from schemas.teacher import Teacher
from dto.teacher import TeacherDTO
from fastapi import FastAPI, Form, Request, UploadFile, File


app = FastAPI()


@app.post("/teachers")
def add_teacher(teacher: TeacherDTO):
    try:
        res = Teacher().save()
    except NotUniqueError as e:
        print(e)
    return {"message": "Hello World"}


# all endpoint for model teachers
@app.get("/teachers")
def get_teachers():
    return Teacher.objects


@app.patch("/teachers")
def update_teacher():
    return {"message": "Hello World"}


@app.delete("/teachers")
def delete_teacher():
    return {"message": "Hello World"}
