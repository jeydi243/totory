from fastapi import APIRouter, File, Form, UploadFile
from fastapi.exceptions import RequestValidationError
from rich import print
from pydantic import ValidationError
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

@router.get("/count")
def get_classes() -> int:
    print("Count all Classes")
    return classe_service.getCountClasses()


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
    return classe_service.getClasseByID(id)
