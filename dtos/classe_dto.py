from pydantic import BaseModel, Field


class ClasseDTO(BaseModel):
    code: str = Field(...)
    description: str = Field(...)
    name:str = Field(alias='title')
