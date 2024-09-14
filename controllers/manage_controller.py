from fastapi import APIRouter

from dtos.org_dto import OrgDTO
from services.manage_service import ManageService

router = APIRouter(
    prefix="/manage",
    tags=["management"],
    responses={404: {"description": "Not found"}},
)
manage_service = ManageService()


@router.post("/organizations")
def registerOrg(organization: OrgDTO):
    print(organization)
    return manage_service.registerOrg(organization)


@router.get("/organizations")
def getOrgs():
    return manage_service.getOrgs()


@router.get("management/documents")
def getDocs():
    return []
