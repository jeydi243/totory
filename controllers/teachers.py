from mongoengine.errors import NotUniqueError
from schemas.teacher import Teacher
from dtos.teacher import TeacherDTO
from fastapi import APIRouter


router = APIRouter(
    prefix="/teachers",
    tags=["management"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
def add_teacher(teacher: TeacherDTO):
    try:
        res = Teacher(**teacher).save()
    except NotUniqueError as e:
        print(e)
    return {"message": "Hello World"}


# all endpoint for model teachers
@router.get("/")
def get_teachers():
    return Teacher.objects


@router.patch("/")
def update_teacher():
    return {"message": "Hello World"}


@router.delete("/")
def delete_teacher():
    return {"message": "Hello World"}
