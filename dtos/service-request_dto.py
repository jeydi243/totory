from datetime import date
from pydantic import BaseModel, Field


class ServiceRequestDTO(BaseModel):
    name: str = Field(...)
    code: str = Field(...)
    description: str = Field(...)
    service_id: str = Field(...)
    student_id: str = Field(...)
    request_date: date = Field(...)
    request_status: str = Field(...)
