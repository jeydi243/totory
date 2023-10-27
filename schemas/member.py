from datetime import date
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field


class ID(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Member(BaseModel):
    id: ID = Field(default_factory=ID, alias="_id")
    name: str = Field(min_length=3, max_length=50)
    date_naissance: date = Field(...)
    email: Optional[EmailStr]
    
class MemberDTO(BaseModel):
    id: ID
    name: str 
    date_naissance: date
    email: Optional[EmailStr]

