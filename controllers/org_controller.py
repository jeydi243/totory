from typing import Union
from fastapi import APIRouter, File, Form, HTTPException, UploadFile, Query, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from rich import print

from dtos.org_dto import OrganizationDTO
from dtos.education_dto import EducationDTO
from services.org_service import OrgService

router = APIRouter(
    prefix="/organizations",
    tags=["Organization"],
    responses={404: {"description": "Not found methods for /organization"}},
)

org_service = OrgService()


@router.get("/bylookups")
def get_organization(lookups_id: Union[str, None] = Query(default=None, max_length=50)):
    print(f"Get all Organization by lookups ID = {lookups_id}")
    return org_service.getOrganizationByLookups(lookups_id)

@router.get("/byparent")
def get_organization(organization_parent_id: Union[str, None] = Query(default=None, max_length=60)):
    print(f"Get all Organization by parent ID = {organization_parent_id}")
    return org_service.getOrganizationByParent(organization_parent_id)


@router.get("")
def get_organization():
    print("Get all Organization")
    return org_service.getOrgs()


@router.post("")
def add_classe(organization: OrganizationDTO):
    try:
        resp = org_service.registerOrg(organization)
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
def update_org(organization: OrganizationDTO):
    try:
        resp = org_service.updateOrganization(organization)
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
def getOrganizationById(id: str):
    return org_service.getById(id)


@router.delete("/{id}")
def deleteOneOrganization(id: str):
    try:
        return org_service.deleteOneOrganization(id)
    except BaseException as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found") 
