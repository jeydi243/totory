from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from member import Member
from dtos.person import PersonDTO

class StudentDTO(PersonDTO):
    content: str = Field(...)
    gpa: float = Field(..., le=4.0)

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "content": "Experiments, Science, and Fashion in Nanophotonics",
                "gpa": "3.0",
            }
        }


class StudentDTO(BaseModel):
    pass


class UpdateStudentModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    content: Optional[str]
    gpa: Optional[float]

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "content": "Experiments, Science, and Fashion in Nanophotonics",
                "gpa": "3.0",
            }
        }
