from fastapi import APIRouter, File, Form, UploadFile
from fastapi.exceptions import RequestValidationError, ValidationError
from rich import print


router = APIRouter(
    prefix="/resources",
    tags=["management"],
    responses={404: {"description": "Not found methods"}},
)
resource_service - ResourceService()

@router.get("")
def get_employees():
    print("To get all employees")
    return employee_service.all_employee()