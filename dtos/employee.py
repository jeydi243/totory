import datetime
from fastapi import UploadFile
from pydantic import Field
from dtos.person import PersonDTO
from pydantic import BaseModel, Field, validator
from datetime import datetime


class EmployeeDTO(PersonDTO):
    domain: str | list[str] = Field(...)
    position: str = Field(max_length=300)
    biography: str = Field(max_length=300)
    hire_date: str | datetime = Field(default=datetime.now())
    onboarding: list = None
    cover_letter: str = Field(max_length=500)

    # @validator("school_start_date")
    # def start_valid(cls, v, values):
    #     print(values)
    #     if v > values["school_end_date"]:
    #         raise ValueError("Start date must be before end date")
    #     return v
