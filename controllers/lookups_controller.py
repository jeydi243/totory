from typing import Union
from fastapi import APIRouter, File, Form, HTTPException, UploadFile, Query, status
from fastapi.responses import JSONResponse
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


@router.get("/byclasse")
def get_lookups(classe_id: Union[str, None] = Query(default=None, max_length=50)):
    print(f"Get all Lookups by classe ID = {classe_id}")
    return lookups_service.getLookupsByClasse(classe_id)


@router.get("")
def get_lookups():
    print("Get all Lookups")
    return lookups_service.getLookups()


@router.post("")
def add_classe(lookups: LookupsDTO):
    try:
        resp = lookups_service.add_lookups(lookups)
        if "erreur" in resp:
            return JSONResponse(content=resp, status_code=status.HTTP_400_BAD_REQUEST) 
        else:
            return resp
    except ValidationError as e:
        print(e)
    except BaseException as er:
        print(er)
        return {"Error": er}
    
@router.patch("")
def add_classe(lookups: LookupsDTO):
    try:
        resp = lookups_service.updateLookups(lookups)
        if "erreur" in resp:
            return JSONResponse(content=resp, status_code=status.HTTP_400_BAD_REQUEST) 
        else:
            return resp
    except ValidationError as e:
        print(e)
    except BaseException as er:
        print(er)
        return {"Error": er}


@router.get("/{id}")
def getLookupsById(id: str):
    return lookups_service.getById(id)


@router.delete("/{id}")
def deleteOneLookups(id: str):
    try:
        return lookups_service.deleteOneLookups(id)
    except BaseException as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found") 
