# 📋 Google Sheets API Setup Guide
## สำหรับระบบทำข้อสอบออนไลน์ 819605

---

## 📌 Overview

เอกสารนี้จะแนะนำวิธีการตั้งค่า Google Sheets API เพื่อบันทึกผลการสอบของนักศึกษาอัตโนมัติ

---

## 🎯 Step 1: สร้าง Google Cloud Project และเปิดใช้งาน API

### 1.1 สร้าง Project ใหม่

1. ไปที่ [Google Cloud Console](https://console.cloud.google.com/)
2. คลิก **Select a project** → **New Project**
3. ตั้งชื่อโปรเจค เช่น `QuizSystem-819605`
4. คลิก **Create**

### 1.2 เปิดใช้งาน Google Sheets API

1. ในเมนูด้านซ้าย คลิก **APIs & Services** → **Library**
2. ค้นหา `Google Sheets API`
3. คลิก **Google Sheets API**
4. คลิก **Enable**

---

## 🔑 Step 2: สร้าง API Key

### 2.1 สร้าง API Key

1. ไปที่ **APIs & Services** → **Credentials**
2. คลิก **+ CREATE CREDENTIALS** → **API key**
3. API Key จะถูกสร้างขึ้น (เช่น `AIzaSyDXXXXXXXXXXXXXXXXXXXXXXXXXXX`)
4. คลิก **RESTRICT KEY** (แนะนำ)

### 2.2 จำกัดการใช้งาน API Key (Optional แต่แนะนำ)

**ตั้งค่า Application restrictions:**
- เลือก **HTTP referrers (web sites)**
- เพิ่ม URL ของเว็บไซต์คุณ เช่น:
  - `http://localhost:8000/*` (สำหรับทดสอบ)
  - `https://yourdomain.com/*` (สำหรับใช้งานจริง)

**ตั้งค่า API restrictions:**
- เลือก **Restrict key**
- เลือกเฉพาะ **Google Sheets API**

3. คลิก **Save**

### 2.3 คัดลอก API Key

```
คัดลอก API Key ที่ได้ เช่น:
AIzaSyDXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## 📊 Step 3: สร้าง Google Spreadsheet

### 3.1 สร้าง Spreadsheet ใหม่

1. ไปที่ [Google Sheets](https://sheets.google.com/)
2. คลิก **+ Blank** เพื่อสร้าง spreadsheet ใหม่
3. ตั้งชื่อ เช่น `819605-Quiz-Results`

### 3.2 สร้าง Sheet สำหรับเก็บผลสอบ

1. เปลี่ยนชื่อ Sheet จาก `Sheet1` เป็น `QuizResults`
2. สร้างหัวตาราง (Row 1):

| A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|
| Timestamp | Student ID | Student Name | Quiz ID | Quiz Title | Score Obtained | Total Points | Percentage | Grade | Time Used | All Answers |

### 3.3 คัดลอก Spreadsheet ID

จาก URL ของ Google Sheets:
```
https://docs.google.com/spreadsheets/d/1ABC123xyz456DEF789/edit
                                      ↑
                          นี่คือ Spreadsheet ID
```

คัดลอกส่วน `1ABC123xyz456DEF789`

### 3.4 ตั้งค่าสิทธิ์การเข้าถึง

1. คลิกปุ่ม **Share** มุมขวาบน
2. ใน **General access** เลือก **Anyone with the link** → **Editor**
3. คลิก **Done**

> ⚠️ **หมายเหตุ:** วิธีนี้ทำให้ใครก็ตามที่มีลิงก์สามารถแก้ไขได้ ถ้าต้องการความปลอดภัยมากขึ้น ให้ใช้ Service Account (ดูในส่วน Advanced)

---

## ⚙️ Step 4: แก้ไขไฟล์ HTML

### 4.1 เปิดไฟล์

เปิดไฟล์ `teaching/819605-2-2568-demo.html`

### 4.2 แก้ไข GOOGLE_SHEETS_CONFIG

ค้นหาบรรทัดที่มี `GOOGLE_SHEETS_CONFIG` และแก้ไขค่าต่อไปนี้:

```javascript
const GOOGLE_SHEETS_CONFIG = {
    // ✏️ 1. แทนที่ด้วย API Key ของคุณ
    API_KEY: 'AIzaSyDXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    
    // ✏️ 2. แทนที่ด้วย Spreadsheet ID ของคุณ
    SPREADSHEET_ID: '1ABC123xyz456DEF789',
    
    // ✏️ 3. ตรวจสอบว่าชื่อ Sheet ตรงกับที่สร้างไว้หรือไม่
    SHEET_NAME: 'QuizResults',
    
    // ✏️ 4. เปลี่ยนเป็น true เพื่อเปิดใช้งาน
    ENABLED: true
};
```

### 4.3 ตัวอย่างการแก้ไข

**ก่อนแก้ไข:**
```javascript
const GOOGLE_SHEETS_CONFIG = {
    API_KEY: 'REPLACE_WITH_YOUR_API_KEY',
    SPREADSHEET_ID: 'REPLACE_WITH_YOUR_SPREADSHEET_ID',
    SHEET_NAME: 'QuizResults',
    ENABLED: false
};
```

**หลังแก้ไข:**
```javascript
const GOOGLE_SHEETS_CONFIG = {
    API_KEY: 'AIzaSyBc1234567890abcdefghijklmnopqrst',
    SPREADSHEET_ID: '1XyZ9876543210AbCdEfGhIjKlMnOpQrStUv',
    SHEET_NAME: 'QuizResults',
    ENABLED: true
};
```

### 4.4 บันทึกไฟล์

กด `Ctrl + S` เพื่อบันทึกไฟล์

---

## 🧪 Step 5: ทดสอบระบบ

### 5.1 เปิดเว็บไซต์

1. เปิด Terminal/PowerShell ที่โฟลเดอร์ `g:\My Drive\profile`
2. รันคำสั่ง:
   ```powershell
   python -m http.server 8000
   ```
3. เปิดเบราว์เซอร์ไปที่: `http://localhost:8000/teaching/819605-2-2568-demo.html`

### 5.2 ทำข้อสอบทดสอบ

1. กรอกข้อมูล:
   - รหัสนักศึกษา: `9999999999`
   - ชื่อ-นามสกุล: `Test Student`
   - เลือกข้อสอบ: **Demo Quiz (ทดสอบระบบ)**
2. คลิก **เริ่มทำข้อสอบ**
3. ตอบคำถามและส่งข้อสอบ

### 5.3 ตรวจสอบผล

1. เปิด Google Sheets ที่สร้างไว้
2. ตรวจสอบว่ามีข้อมูลถูกบันทึกในแถวใหม่หรือไม่
3. ตรวจสอบค่าต่าง ๆ ในแต่ละคอลัมน์

### 5.4 ตรวจสอบ Console

เปิด Developer Tools (F12) ในเบราว์เซอร์:
- ถ้าสำเร็จ จะเห็น: `✅ Results submitted to Google Sheets successfully`
- ถ้าล้มเหลว จะเห็น error message พร้อมรายละเอียด

---

## 🔍 Troubleshooting

### ❌ Error: "The API key doesn't have the necessary permissions"

**สาเหตุ:** API Key ไม่มีสิทธิ์เข้าถึง Google Sheets API

**แก้ไข:**
1. ไปที่ [Google Cloud Console](https://console.cloud.google.com/)
2. เลือก Project ของคุณ
3. ไปที่ **APIs & Services** → **Credentials**
4. คลิก API Key ที่สร้างไว้
5. ใน **API restrictions** ตรวจสอบว่าเลือก **Google Sheets API** แล้ว
6. คลิก **Save**

---

### ❌ Error: 404 "Requested entity was not found"

**สาเหตุ:** Spreadsheet ID ไม่ถูกต้อง หรือไม่มีสิทธิ์เข้าถึง

**แก้ไข:**
1. ตรวจสอบ Spreadsheet ID ว่าคัดลอกถูกต้อง
2. ตรวจสอบว่า Spreadsheet มีการตั้งค่า **Anyone with the link** เป็น **Editor**
3. ลองเปิด Spreadsheet ใน Incognito Mode ดูว่าเข้าถึงได้หรือไม่

---

### ❌ Error: 400 "Unable to parse range"

**สาเหตุ:** ชื่อ Sheet ไม่ตรงกับที่ตั้งค่าไว้

**แก้ไข:**
1. เปิด Google Sheets
2. ตรวจสอบชื่อ Sheet/Tab (ด้านล่าง)
3. แก้ไข `SHEET_NAME` ในไฟล์ HTML ให้ตรงกับชื่อจริง

---

### ❌ Error: 403 "The request is missing a valid API key"

**สาเหตุ:** API Key ไม่ถูกต้อง หรือไม่ได้กรอก

**แก้ไข:**
1. ตรวจสอบว่าคัดลอก API Key ถูกต้อง
2. ตรวจสอบว่าไม่มีเว้นวรรคหรือตัวอักษรพิเศษเกิน
3. ลอง Generate API Key ใหม่

---

### ❌ ข้อมูลบันทึกใน localStorage แต่ไม่ส่งไป Google Sheets

**สาเหตุ:** `ENABLED: false` หรือมี error ในการเชื่อมต่อ

**แก้ไข:**
1. ตรวจสอบว่า `ENABLED: true`
2. เปิด Console (F12) ดู error message
3. ตรวจสอบการเชื่อมต่ออินเทอร์เน็ต

---

### ⚠️ การแก้ไขไฟล์แล้วไม่เห็นผล

**สาเหตุ:** Browser cache

**แก้ไข:**
1. กด `Ctrl + Shift + R` (Hard Refresh)
2. หรือเปิด Developer Tools (F12) → เลือก **Disable cache** ใน Network tab
3. หรือเปิดในโหมด Incognito

---

## 🔒 Advanced: ใช้ Service Account (สำหรับความปลอดภัยสูง)

### ทำไมต้องใช้ Service Account?

- ไม่ต้องเปิด Spreadsheet เป็น Public
- ควบคุมสิทธิ์การเข้าถึงได้ดีกว่า
- เหมาะสำหรับการใช้งานจริง

### วิธีตั้งค่า

1. ไปที่ [Google Cloud Console](https://console.cloud.google.com/)
2. **APIs & Services** → **Credentials**
3. **+ CREATE CREDENTIALS** → **Service account**
4. ตั้งชื่อ Service Account และคลิก **Create**
5. คลิก **Done**
6. คลิกที่ Service Account ที่สร้าง
7. ไปที่แท็บ **Keys**
8. **ADD KEY** → **Create new key** → เลือก **JSON**
9. ไฟล์ JSON จะถูกดาวน์โหลด

### แก้ไขโค้ด

**ต้องใช้ Backend (Node.js, Python, PHP)**

ไม่สามารถใช้ Service Account ใน JavaScript บนเบราว์เซอร์ได้โดยตรง (เพราะเป็นการเปิดเผย Private Key)

**ตัวอย่าง Backend ด้วย Node.js:**

```javascript
const { google } = require('googleapis');
const express = require('express');
const app = express();

app.use(express.json());

// โหลด Service Account credentials
const auth = new google.auth.GoogleAuth({
    keyFile: 'path/to/service-account-key.json',
    scopes: ['https://www.googleapis.com/auth/spreadsheets']
});

app.post('/submit-quiz', async (req, res) => {
    const sheets = google.sheets({ version: 'v4', auth });
    const { results } = req.body;
    
    try {
        await sheets.spreadsheets.values.append({
            spreadsheetId: 'YOUR_SPREADSHEET_ID',
            range: 'QuizResults!A:K',
            valueInputOption: 'RAW',
            resource: {
                values: [[
                    new Date().toLocaleString(),
                    results.studentId,
                    results.studentName,
                    // ... ข้อมูลอื่น ๆ
                ]]
            }
        });
        
        res.json({ success: true });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

app.listen(3000);
```

---

## 📚 สรุป

### ✅ สิ่งที่ต้องแทนที่ในไฟล์ HTML:

```javascript
const GOOGLE_SHEETS_CONFIG = {
    API_KEY: 'YOUR_ACTUAL_API_KEY_HERE',              // ← แทนที่ตรงนี้
    SPREADSHEET_ID: 'YOUR_ACTUAL_SPREADSHEET_ID',     // ← แทนที่ตรงนี้
    SHEET_NAME: 'QuizResults',                        // ← ตรวจสอบชื่อ Sheet
    ENABLED: true                                     // ← เปลี่ยนเป็น true
};
```

### 📝 Checklist

- [ ] สร้าง Google Cloud Project
- [ ] เปิดใช้งาน Google Sheets API
- [ ] สร้าง API Key
- [ ] จำกัดการใช้งาน API Key (Optional)
- [ ] สร้าง Google Spreadsheet
- [ ] สร้าง Sheet ชื่อ `QuizResults`
- [ ] เพิ่มหัวตาราง (11 คอลัมน์)
- [ ] ตั้งค่าสิทธิ์ "Anyone with the link" เป็น "Editor"
- [ ] คัดลอก API Key
- [ ] คัดลอก Spreadsheet ID
- [ ] แก้ไขไฟล์ HTML (`GOOGLE_SHEETS_CONFIG`)
- [ ] เปลี่ยน `ENABLED` เป็น `true`
- [ ] บันทึกไฟล์
- [ ] ทดสอบระบบ
- [ ] ตรวจสอบข้อมูลใน Google Sheets

---

## 📞 ติดต่อ

หากมีปัญหาหรือข้อสงสัย กรุณาติดต่อ:
- อาจารย์ผู้สอน
- IT Support

---

## 📄 License

เอกสารนี้สำหรับการใช้งานในวิชา 819605 Discrete Mathematics เท่านั้น

---

**อัพเดทล่าสุด:** 2024
**เวอร์ชัน:** 1.0
