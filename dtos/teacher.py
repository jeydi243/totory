from pydantic import BaseModel, Field, EmailStr, Optional
from dtos.person import PersonDTO

class Teacher(PersonDTO):
    resume_file: Field(...)