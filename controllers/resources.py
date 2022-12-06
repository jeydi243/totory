from fastapi import APIRouter, File, Form, UploadFile
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
def get_employees():
    print("To get all employees")
    return resource_service.get()