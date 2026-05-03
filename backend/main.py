from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .database import engine, get_db, Base
from .models import ItemDB, ItemCreate, Item

# สร้างตารางใน Database (ถ้ายังไม่มี)
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/items/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = ItemDB(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/", response_model=List[Item])
def read_items(db: Session = Depends(get_db)):
    return db.query(ItemDB).all()

@app.get("/")
def root():
    return {"status": "Backend is running with Database connection"}
