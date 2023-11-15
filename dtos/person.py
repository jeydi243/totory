from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, validator

class PersonDTO(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    middle_name: str = Field(...)
    address: str = Field(max_length=100, min_length=5)
    gender: str = Field(
        max_length=1,
        min_length=1,
    )
    telephones: str | list[str] = Field(min_items=1, max_items=3)
    personal_email: str | list[str] = Field(min_items=1, max_items=3)
    birthday: str = Field(..., format="%Y-%m-%d")

  
        
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        orm_mode = True

    # @validator("name")
    # def name_must_contain_space(cls, v):
    #     if " " not in v:
    #         raise ValueError("Must contain a space, it seems like you forgot it lastname or middle name")
    #     return v.title()

    @validator("personal_email")
    def isemail(cls, v: str, values, **kwargs):
        if all(("@" in email == True) for email in values):
            raise ValueError(f"There is invalid email in emails:\n \t {v}")
        return v

    @validator("gender")
    def username_alphanumeric(cls, v: str):
        assert len(v) == 1, "must be 1 characters"
        return v

    @validator("telephones")
    def telephone_is_valid(cls, v: List[str]):
        if not all(val.isdigit() for val in v):
            raise ValueError("Must be a valid telephone number..")
        return v

    @validator("birthday")
    def is_adult(cls, v: str):
        today = datetime.now().year
        till = datetime.strptime(v, "%Y-%m-%d").year
        till_birth = today - till
        if till_birth <= 10:
            raise ValueError(f"{till_birth} years old. You are not an adult")
        return v
