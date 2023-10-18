from fastapi import APIRouter
from dtos.org_dto import ServiceDTO
from services.manage_service import ManageService
from services.services_service import Service

router = APIRouter(
    prefix="/services",
    tags=["services"],
    responses={404: {"description": "Not found"}},
)
service = Service()


@router.post("/service")
def registerService(service: ServiceDTO):
    print(service)
    return service.add_service(service)


@router.get("/service")
def getServices():
    return service.all_services()


@router.get("management/documents")
def getDocs():
    return []
