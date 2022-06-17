from typing_extensions import TypedDict
from pydantic import BaseModel, Field


class Name(TypedDict):
    first: str
    last: str
    middle: str


class PersonDTO(BaseModel):
    name: str | Name
    address: str = Field(max_length=100, min_length=5)
    gender: str = Field(max_length=1, min_length=1)
    telephones: str | list[str] = Field(min_items=1, max_items=3)
    email: str | list[str] = Field(min_items=1, max_items=3)
