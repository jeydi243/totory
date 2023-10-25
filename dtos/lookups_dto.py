from pydantic import BaseModel, Field


class LookupsDTO(BaseModel):
    code: str = Field(...)
    description: str = Field(...)
    classe_id: str = Field(...)
