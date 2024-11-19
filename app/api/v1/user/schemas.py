from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    first_name: str
    last_name: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
    created_at: datetime
