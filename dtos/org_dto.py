from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, Field, validator


class OrganizationDTO(BaseModel):
    id: Optional[str] = Field(None, exclude=True)
    name: str = Field(...)
    code: str = Field(...)
    description: str = Field(...)
    active_date: datetime | str = Field(...)
    end_date: Optional[datetime | str] = Field(None)
    organization_parent_id: Optional[str] = Field(None, exclude=True)
    lookup_id: str | None = Field(...)
