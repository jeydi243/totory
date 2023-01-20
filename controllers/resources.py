from rich import print
from fastapi import APIRouter, File, Form, UploadFile
from fastapi.exceptions import RequestValidationError, ValidationError
from services.resource_service import ResourceService


router = APIRouter(
    prefix="/resources",
    tags=["management"],
    responses={404: {"description": "Not found methods"}},
)
resource_service = ResourceService()


@router.get("")
def get_resources():
    print("To get resources info")
    return resource_service.get()


@router.post("")
def add_resource(img: UploadFile = Form()):
    print(f"To add resource info {img}")
    return resource_service.add(img)


@router.delete("/{id}")
def add_resource(id: str):
    return resource_service.deleteByID(id)
