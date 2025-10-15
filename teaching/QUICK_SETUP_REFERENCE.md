# ⚡ Quick Setup Reference Card

## 🎯 3 สิ่งที่ต้องแทนที่

### 1️⃣ API Key
**ที่หา:** [Google Cloud Console](https://console.cloud.google.com/) → APIs & Services → Credentials → Create API Key

**ตำแหน่งในโค้ด:**
```javascript
API_KEY: 'REPLACE_WITH_YOUR_API_KEY'
```

**ตัวอย่าง:**
```javascript
API_KEY: 'AIzaSyBc1234567890abcdefghijklmnopqrst'
```

---

### 2️⃣ Spreadsheet ID
**ที่หา:** จาก URL ของ Google Sheets
```
https://docs.google.com/spreadsheets/d/1ABC123xyz456DEF789/edit
                                      ^^^^^^^^^^^^^^^^^^^^^^^
                                      นี่คือ Spreadsheet ID
```

**ตำแหน่งในโค้ด:**
```javascript
SPREADSHEET_ID: 'REPLACE_WITH_YOUR_SPREADSHEET_ID'
```

**ตัวอย่าง:**
```javascript
SPREADSHEET_ID: '1XyZ9876543210AbCdEfGhIjKlMnOpQrStUv'
```

---

### 3️⃣ เปิดใช้งาน
**ตำแหน่งในโค้ด:**
```javascript
ENABLED: false  // เปลี่ยนเป็น true
```

**ตัวอย่าง:**
```javascript
ENABLED: true
```

---

## 📊 ตารางใน Google Sheets

### หัวคอลัมน์ (Row 1):

| A | B | C | D | E |
|---|---|---|---|---|
| Timestamp | Student ID | Student Name | Quiz ID | Quiz Title |

| F | G | H | I | J | K |
|---|---|---|---|---|---|
| Score Obtained | Total Points | Percentage | Grade | Time Used | All Answers |

---

## ✅ Checklist สั้น

- [ ] สร้าง API Key
- [ ] สร้าง Google Spreadsheet
- [ ] ตั้งค่าสิทธิ์ "Anyone with the link → Editor"
- [ ] คัดลอก API Key → แทนใน `API_KEY`
- [ ] คัดลอก Spreadsheet ID → แทนใน `SPREADSHEET_ID`
- [ ] เปลี่ยน `ENABLED: false` → `true`
- [ ] บันทึกไฟล์
- [ ] ทดสอบ

---

## 🔍 ตรวจสอบว่าใช้งานได้

### ดูใน Browser Console (F12):
- ✅ สำเร็จ: `Results submitted to Google Sheets successfully`
- ❌ ล้มเหลว: Error message พร้อมคำแนะนำ

### ดูใน Google Sheets:
- มีข้อมูลแถวใหม่หลังส่งข้อสอบ

---

## 📱 Quick Links

- [Google Cloud Console](https://console.cloud.google.com/)
- [Google Sheets](https://sheets.google.com/)
- [Full Setup Guide](./GOOGLE_SHEETS_SETUP_GUIDE.md)

---

**สำคัญ:** อ่าน [GOOGLE_SHEETS_SETUP_GUIDE.md](./GOOGLE_SHEETS_SETUP_GUIDE.md) เพื่อดูรายละเอียดทั้งหมด
