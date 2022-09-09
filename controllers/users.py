from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found methods"}},
)


@router.get("/login")
def login(user: None):
    print(user)


@router.get("logout")
def logout():
    pass
