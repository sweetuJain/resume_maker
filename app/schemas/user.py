from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from datetime import datetime


class UserBase(BaseModel):
    email_address: EmailStr
    username: str = Field(min_length=3, max_length=50)
    profile_payload:  Optional[dict] = Field(default_factory=dict)
    phone_number: str = Field(
        pattern=r"^[1-9][0-9]{11}$",
        description="12 digit phone number: country code (2) + mobile (10), no +"
    )

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)
    
class UserOut(UserBase):
    id: UUID
    created_at: datetime