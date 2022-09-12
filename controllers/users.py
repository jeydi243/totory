from fastapi import APIRouter

from dtos.user_dto import UserDTO

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found methods"}},
)


@router.post("/login")
def login(user: UserDTO):
    print(user)
    return {"token": "123456789"}


@router.get("/logout")
def logout():
    return {"token": None}
