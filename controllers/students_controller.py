from mongoengine.errors import NotUniqueError
from schemas.student import Student
from fastapi import APIRouter
from dtos.student_dto import StudentDTO
from services.students_service import StudentService

router = APIRouter(
    prefix="/students",
    tags=["management"],
    responses={404: {"description": "Not found methods"}},
)
student_service = StudentService()


@router.post("/")
def add_student(student: StudentDTO):
    try:
        res = student_service.add_student(student)
    except NotUniqueError as e:
        print(e)
    return {"message": "Hello World"}


# all endpoint for model students
@router.get("")
def get_students():
    return student_service.all_students()


@router.put("/")
def update_student():
    return {"message": "Method must be implemented"}


@router.delete("/")
def delete_student():
    return {"message": "Method must be implemented"}
