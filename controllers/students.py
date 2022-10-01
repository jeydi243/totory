from mongoengine.errors import NotUniqueError
from schemas.student import Student
from fastapi import APIRouter
from dtos.student import StudentDTO

router = APIRouter(
    prefix="/students",
    tags=["management"],
    responses={404: {"description": "Not found methods"}},
)


@router.post("/")
def add_student(student: StudentDTO):
    try:
        res = Student().save()
    except NotUniqueError as e:
        print(e)
    return {"message": "Hello World"}


# all endpoint for model students
@router.get("")
def get_students():
    return []


@router.patch("/")
def update_student():
    return {"message": "Method must be implemented"}


@router.delete("/")
def delete_student():
    return {"message": "Method must be implemented"}
