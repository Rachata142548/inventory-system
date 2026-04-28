# ใช้ Node.js เวอร์ชั่นล่าสุด
FROM node:18-alpine

# กำหนด Working Directory
WORKDIR /app

# คัดลอก package.json และ install dependencies
COPY package*.json ./
RUN npm install

# คัดลอกไฟล์โปรเจกต์ทั้งหมด
COPY . .

# Build โปรเจกต์
RUN npm run build

# รันแอปพลิเคชัน
CMD ["npm", "start"]
