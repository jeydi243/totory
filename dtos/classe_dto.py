from pydantic import BaseModel, Field


class ClasseDTO(BaseModel):
    name:str = Field(alias='title')
    code: str = Field(...)
    description: str = Field(...)
