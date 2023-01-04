

router = APIRouter(
    prefix="/employees",
    tags=["management"],
    responses={404: {"description": "Not found methods"}},
)


