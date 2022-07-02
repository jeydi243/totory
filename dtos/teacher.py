from pydantic import Field, EmailStr

from dtos.person import PersonDTO


class TeacherDTO(PersonDTO):
    resume_file: str = Field(...)
