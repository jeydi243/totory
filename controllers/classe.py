from fastapi import APIRouter, File, Form, UploadFile
from fastapi.exceptions import RequestValidationError, ValidationException
from rich import print

from dtos.classe_dto import CourseDTO
from dtos.education_dto import EducationDTO
from services.classe_service import CourseService

router = APIRouter(
    prefix="/classes",
    responses={404: {"description": "Not found methods for /classes"}},
)

classe_service = CourseService()


@router.get("")
def get_classes():
    print("Get all Classes")
    return classe_service.getClasses()


@router.post("")
def add_employee(course: CourseDTO):
    try:
        print(course)
        created_course = classe_service.add_course(course)
        print(f"{created_course=}")
        return created_course
    except BaseException as er:
        print(er)
        return {"Error": er}
    except ValidationException as e:
        print(e)


@router.get("/{id}")
def getById(id: str):
    return classe_service.getById(id)
