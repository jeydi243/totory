from rich import print
from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import FileResponse, Response, StreamingResponse
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


@router.get("/stream/{file_id}")
def stream_resource(file_id: str):
    print("To stream resource")
    response = StreamingResponse(content=resource_service.stream(file_id))
    return response


@router.get("/download/{file_id}")
def download_resource(file_id: str):
    print("To download resource")
    file = resource_service.download(file_id)
    headers = {"Content-Disposition": f'attachment; filename="{file.filename}"'}

    if file:
        response = Response(file.read(), headers=headers)
        return response
    else:
        return "There is no file"


@router.post("")
def add_resource(img: UploadFile = Form()):
    print(f"To add resource info {img}")
    return resource_service.add(img)


@router.delete("/{id}")
def delete_by_ID(id: str):
    return resource_service.deleteByID(id)
