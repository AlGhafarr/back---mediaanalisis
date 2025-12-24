from pydantic import BaseModel, Emailstr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email : Emailstr
    full_name: Optional[str] = None
    role: str = "viewer"

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email Optional[Emailstr] = None
    full_name: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None

class UserResponse(UserBase):
    id = int
    is_active: bool
    create_at: datetime

    class Config:
        from_attribute = True

class Token(BaseModel):
    access_token: str
    token_type: String
    
class LoginRequest(BaseModel):
    username: str
    password: str
