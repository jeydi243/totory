from fastapi import APIRouter, File, Form, UploadFile
from fastapi.exceptions import  ValidationException
from rich import print

from dtos.lookups_dto import LookupsDTO
from dtos.education_dto import EducationDTO
from services.lookups_service import LookupsService

router = APIRouter(
    prefix="/lookups",
    responses={404: {"description": "Not found methods for /lookups"}},
)

lookups_service = LookupsService()


@router.get("")
def get_lookups():
    print("Get all Lookupss")
    return lookups_service.getLookupss()


@router.post("")
def add_classe(classe: LookupsDTO):
    try:
        print(classe)
        created_lookups = lookups_service.add_lookups(classe)
        print(f"{created_lookups=}")
        return created_lookups
    except BaseException as er:
        print(er)
        return {"Error": er}
    except ValidationException as e:
        print(e)


@router.get("/{id}")
def getById(id: str):
    return lookups_service.getById(id)
