from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class OrderCreate(BaseModel):
    customer_name: str
    customer_email: str
    product_name: str
    quantity: int
    price: float


class OrderUpdate(BaseModel):
    status: str


class OrderResponse(BaseModel):
    id: int
    customer_name: str
    customer_email: str
    product_name: str
    quantity: int
    price: float
    status: str
    created_at: Optional[datetime]

    class Config:
        from_attributes = True
