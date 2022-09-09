from pydantic import BaseModel, Field


class EducationDTO(BaseModel):
    from_school: str = Field(...)
    name: str = Field(...)
    end: str = Field(...)
    start: str = Field(...)
    description: str = Field(
        min_length=10,
    )
