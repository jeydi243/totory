from datetime import date
from typing import List
from pydantic import BaseModel, Field


class ServiceRequestDTO(BaseModel):
    service_id: str = Field(...)
    student_id: str = Field(...)
    priority: str = Field(...)
    attachements: List[str] = Field(...)
    request_date: date = Field(...)
    request_status: str = Field(...)
