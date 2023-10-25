from datetime import datetime
from pydantic import BaseModel
from pydantic import BaseModel, Field, validator


class OrgDTO(BaseModel):
    id: str | None = Field(...)
    name: str = Field(...)
    code: str = Field(...)
    description: str = Field(...)
    date_desactivation: datetime | None = Field(...)
    date_creation: datetime = Field(...)
    organization_parent_id: str | None = Field(...)
