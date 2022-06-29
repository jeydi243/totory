from main import app
from mongoengine.errors import NotUniqueError
from schemas.student import Student
from fastapi import APIRouter, Depends, FastAPI, Form, Request, UploadFile, File
from ..dependencies import get_token_header


router = APIRouter(
    prefix="/students",
    tags=["management"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found methods"}},
)


@router.post("/")
def add_student():
    try:
        res = Student().save()
    except NotUniqueError as e:
        print(e)
    return {"message": "Hello World"}


# all endpoint for model students
@router.get("/")
def get_students():
    return Student.objects


@router.patch("/")
def update_student():
    return {"message": "Method must be implemented"}


@router.delete("/")
def delete_student():
    return {"message": "Method must be implemented"}
