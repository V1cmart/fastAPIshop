from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime


class UserBase(BaseModel):
    name: str = Field(..., max_length=100)
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=70)


class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8, max_length=70)


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# class UserWithOrders(UserResponse):
#     orders: List["OrderResponse"] = []
#     cart_items: List["CartItemResponse"] = []
