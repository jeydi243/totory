from typing import Optional
from pydantic import BaseModel, Field


class LookupsDTO(BaseModel):
    id: Optional[str] = Field(None, exclude=True)
    name: str = Field(...)
    code: str = Field(...)
    description: str = Field(...)
    classe_id: Optional[str] = Field(None, exclude=True)
    parent_lookups_id: Optional[str] = Field(None, exclude=True)
