from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import  FileResponse
from fastapi.exceptions import RequestValidationError, ValidationError
from rich import print

from services.resource_service import ResourceService


router = APIRouter(
    prefix="/resources",
    tags=["management"],
    responses={404: {"description": "Not found methods"}},
)
resource_service = ResourceService()


@router.get("")
def get_resources():
    print("To get all resources")
    return resource_service.get()

@router.post("")
def add_resource(img: bytes = File()):
    print("Add resource")
    return resource_service.add(img)

@router.get("/info/{id}")
def get_resource_info(id: str):
    print(f"Get resource info with {id=}")
    return resource_service.get_resource_info(id)

@router.get("/file/{id}")
def get_resource_file(id: str):
    print(f"Get resource file for {id=}")
    return resource_service.get_resource_file(id)

@router.get("/download/{id}")
def get_resource_file(id: str):
    print(f"Get resource file for {id=}")
    return resource_service.download_resource(id)
