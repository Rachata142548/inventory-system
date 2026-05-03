import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ตรวจสอบค่าจาก Environment Variable ถ้าไม่มีให้ใช้ค่าเริ่มต้นสำหรับรันในเครื่อง (Local)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db/inventory_db")

# Render มักจะส่งค่าเริ่มต้นเป็น postgres:// ซึ่ง SQLAlchemy ต้องการ postgresql://
if SQLALCHEMY_DATABASE_URL and SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency สำหรับสร้าง Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
