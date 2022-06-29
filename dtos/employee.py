import datetime
from fastapi import UploadFile
from pydantic import Field
from dtos.person import PersonDTO


class EmployeeDTO(PersonDTO):
    cover_letter: str = Field(...)
    domain: str | list[str] = Field(...)
    resume_file: UploadFile = Field(UploadFile)

    school_name: str = Field(...)
    school_diploma_file: UploadFile = Field(UploadFile)
    school_start_date: str | datetime.date = Field(...)
    school_end_date: str | datetime.date = Field(...)
