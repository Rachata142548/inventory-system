from sqlalchemy import Column, Integer, String, Float
from .database import Base
from pydantic import BaseModel
from typing import Optional

# --- SQLAlchemy Model (สำหรับสร้างตารางใน DB) ---
class ItemDB(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

# --- Pydantic Schemas (สำหรับรับ-ส่งข้อมูล API) ---
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True
