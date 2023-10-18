from pydantic import BaseModel, Field


class ServiceDTO(BaseModel):
    code: str = Field(...)
    name: str = Field(alias="title")
    contact: str = Field(...)
    website: str = Field(...)
    description: str = Field(...)
