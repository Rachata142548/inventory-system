# ใช้ Node.js เวอร์ชั่นล่าสุด
FROM node:20-alpine

# กำหนด Working Directory
WORKDIR /app

# คัดลอก package.json และ install dependencies
COPY package*.json ./
RUN npm install

# คัดลอกไฟล์โปรเจกต์ทั้งหมด
COPY . .

# --- เพิ่มส่วนนี้เพื่อให้ Docker รับค่าจาก Render ได้ ---
ARG NEXT_PUBLIC_API_URL
ENV NEXT_PUBLIC_API_URL=$NEXT_PUBLIC_API_URL
# --------------------------------------------------

# Build โปรเจกต์
RUN npm run build

# รันแอปพลิเคชัน
CMD ["npm", "start"]
