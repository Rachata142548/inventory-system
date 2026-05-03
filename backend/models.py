from pydantic import BaseModel
from typing import Optional

# โครงสร้างข้อมูลสำหรับรับเข้า (สร้างใหม่)
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

# โครงสร้างข้อมูลสำหรับส่งออก (มี ID)
class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True
