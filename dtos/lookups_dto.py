from pydantic import BaseModel, Field


class LookupsDTO(BaseModel):
    name: str = Field(alias="title")
    code: str = Field(...)
    description: str = Field(...)
    classe_id: str = Field(...)
