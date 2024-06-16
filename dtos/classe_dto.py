from pydantic import BaseModel, Field


class ClasseDTO(BaseModel):
    name:str = Field(...)
    code: str = Field(...)
    description: str = Field(...)
