from fastapi import APIRouter, File, Form, UploadFile
from fastapi.exceptions import RequestValidationError, ValidationError
from rich import print

from dtos.course_dto import CourseDTO
from dtos.education_dto import EducationDTO
from services.course_service import CourseService

router = APIRouter(
    prefix="/courses",
    responses={404: {"description": "Not found methods"}},
)

course_service = CourseService()


@router.get("")
def get_courses():
    print("Get all Courses")
    return course_service.getCourses()


@router.post("")
def add_employee(course: CourseDTO):
    try:
        print(course)
        created_course = course_service.add_course(course)
        print(f"{created_course=}")
        return created_course
    except BaseException as er:
        print(er)
        return {"Error": er}
    except ValidationError as e:
        print(e.json())


@router.get("/{id}")
def getById(id: str):
    return course_service.getById(id)
