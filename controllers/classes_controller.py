from fastapi import APIRouter, File, Form, UploadFile
from fastapi.exceptions import RequestValidationError, ValidationError
from rich import print

from dtos.classe_dto import ClasseDTO
from dtos.education_dto import EducationDTO
from services.classe_service import ClasseService

router = APIRouter(
    prefix="/classes",
    tags=["Classes"],
    responses={404: {"description": "Not found methods for /classes"}},
)

classe_service = ClasseService()


@router.get("")
def get_classes():
    print("Get all Classes")
    return classe_service.getClasses()


@router.post("")
def add_classe(classe: ClasseDTO):
    try:
        print(classe)
        created_classe = classe_service.add_classe(classe)
        print(f"{created_classe=}")
        return created_classe
    except ValidationError as e:
        print(e)
    except BaseException as er:
        print(er)
        return {"Error": er}
    


@router.get("/{id}")
def getById(id: str):
    return classe_service.getById(id)
