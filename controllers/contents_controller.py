from fastapi import APIRouter, File, Form, UploadFile
from fastapi.exceptions import RequestValidationError, ValidationException
from rich import print

from dtos.content_dto import ContentDTO
from dtos.education_dto import EducationDTO
from services.content_service import ContentService

router = APIRouter(
    prefix="/contents",
    responses={404: {"description": "Not found methods"}},
)

content_service = ContentService()


@router.get("")
def get_contents():
    print("Get all Contents")
    return content_service.getContents()


@router.post("")
def add_employee(content: ContentDTO):
    try:
        print(content)
        created_content = content_service.add_content(content)
        print(f"{created_content=}")
        return created_content
    except BaseException as er:
        print(er)
        return {"Error": er}
    except ValidationException as e:
        print(e)


@router.get("/{id}")
def getById(id: str):
    return content_service.getById(id)
