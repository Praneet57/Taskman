from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from models import PriorityEnum, StatusEnum

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = ""
    priority: Optional[PriorityEnum] = PriorityEnum.medium
    status: Optional[StatusEnum] = StatusEnum.pending
    deadline: Optional[datetime] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[PriorityEnum] = None
    status: Optional[StatusEnum] = None
    deadline: Optional[datetime] = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    priority: PriorityEnum
    status: StatusEnum
    deadline: Optional[datetime]
    created_at: datetime
    class Config:
        from_attributes = True
