# ใช้ Python เวอร์ชั่น 3.11 หรือสูงกว่า
FROM python:3.11-slim

# กำหนด Working Directory
WORKDIR /app

# คัดลอกไฟล์ requirements.txt และติดตั้ง library
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกโค้ดทั้งหมด
COPY . .

# รันแอปพลิเคชันด้วย uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
