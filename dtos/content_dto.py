from pydantic import BaseModel, Field


class ContentDTO(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    authors: list = Field(...)
    expireDate: str | None = Field(default=None)
    parts: list[dict] = Field(default=[])
