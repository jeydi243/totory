from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError, ValidationException
from fastapi.responses import JSONResponse

from dtos.documentDTO import DocumentDTO
from services.document_service import DocumentService

router = APIRouter(
    prefix="/management/documents",
    tags=["management"],
    responses={404: {"description": "Not found methods"}},
)

doc_service = DocumentService()


@router.post("")
def add_document(document: DocumentDTO):
    try:
        # print(document)
        doc = doc_service.add(document)
        print(f"Created document {doc}")
        return doc
    except ValidationException as e:
        print(e.json())
    except BaseException as er:
        print(f"Error un detected: {er}")
        return {"f": "ff"}


@router.get("", response_model=DocumentDTO)
def getDocuments():
    all_docs = doc_service.getDocuments()
    print(f"DONC: {all_docs}")
    return JSONResponse(content=jsonable_encoder(all_docs))
