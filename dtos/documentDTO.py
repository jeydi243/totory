from pydantic import BaseModel, Field


class DocumentDTO(BaseModel):
    
    name :str = Field(...)
    code :str = Field(...)
    description :str = Field(...)