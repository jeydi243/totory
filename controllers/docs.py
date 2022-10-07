from fastapi import APIRouter
from dtos.documentDTO import DocumentDTO
from fastapi.exceptions import RequestValidationError, ValidationError
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
    except ValidationError as e:
        print(e.json())
    except BaseException as er:
        print(f"Error un detected: {er}")
        return {"f": "ff"}


@router.get("")
def getDocuments():
    print("To get all documents")
    all_docs = doc_service.getDocuments()
    print(f"DONC: {all_docs}")
    return list(all_docs)
