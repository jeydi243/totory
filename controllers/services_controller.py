from turtle import title
from fastapi import APIRouter, UploadFile, Form, File
from typing import Annotated
from fastapi.responses import FileResponse
from dtos.service_dto import ServiceDTO
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


@router.get("/service", description="Get all services")
def getServices():
    return service.all_services()


@router.put("/service", description="Update the image of service", summary="Update the image of service", response_description="Object containing the filename and other information of file")
def updateFile(img: UploadFile, form: Annotated[str, Form()]):
    return {"content": "", "filename": img.filename, "content_type": img.content_type}
    return FileResponse(
        filename="I Love How To use Fastapi",
        status_code=200,
    )


@router.get("management/documents")
def getDocs():
    return []
