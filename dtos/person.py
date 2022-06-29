from datetime import datetime
from typing_extensions import TypedDict
from pydantic import BaseModel, Field, validator


class Name(TypedDict):
    first: str
    last: str
    middle: str


class PersonDTO(BaseModel):
    name: str | Name
    address: str = Field(max_length=100, min_length=5)
    gender: str = Field(
        max_length=1,
        min_length=1,
    )
    telephones: str | list[str] = Field(min_items=1, max_items=3)
    email: str | list[str] = Field(min_items=1, max_items=3)
    birthday: str = Field(..., format="%Y-%m-%d")

    @validator("name")
    def name_must_contain_space(cls, v):
        if " " not in v:
            raise ValueError("Must contain a space, it seems like you forgot it lastname or middle name")
        return v.title()

    @validator("email")
    def isemail(cls, v: str, values, **kwargs):
        if "email" in values:
            raise ValueError("This is not valid Email")
        return v

    @validator("gender")
    def username_alphanumeric(cls, v: str):
        assert len(v) == 1, "must be 1 characters"
        return v

    @validator("birthday")
    def is_adult(cls, bday: str):
        today = datetime.now().today()
        till = datetime.strptime(bday, "%Y-%m-%d")
        till_birth = today - bday
        if till_birth < 2:
            raise ValueError("You are not an adult")
