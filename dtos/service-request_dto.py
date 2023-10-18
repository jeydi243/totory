from pydantic import BaseModel, Field


class ServiceRequestDTO(BaseModel):
    name:str = Field(alias='title')
    code: str = Field(...)
    description: str = Field(...)
    service_id: str = Field(...)
    student_id: str = Field(...)
