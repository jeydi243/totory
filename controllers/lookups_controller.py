from fastapi import APIRouter, File, Form, UploadFile
from pydantic import ValidationError
from rich import print

from dtos.lookups_dto import LookupsDTO
from dtos.education_dto import EducationDTO
from services.lookups_service import LookupsService

router = APIRouter(
    prefix="/lookups",
    tags=["Lookups"],
    responses={404: {"description": "Not found methods for /lookups"}},
)

lookups_service = LookupsService()



@router.get("")
def get_lookups():
    print("Get all Lookups")
    return lookups_service.getLookups()


@router.get("/")
def get_lookups(classe_id: str):
    print(f"Get all Lookups by classe = {classe_id}")
    return lookups_service.getLookupsByClasse(classe_id)


@router.post("")
def add_classe(classe: LookupsDTO):
    print("Add one Lookups")
    try:
        print(classe)
        created_lookups = lookups_service.add_lookups(classe)
        print(f"{created_lookups=}")
        return created_lookups
    except BaseException as er:
        print(er)
        return {"Error": er}
    except ValidationError as e:
        print(e)


@router.get("/{id}")
def getById(id: str):
    return lookups_service.getById(id)
