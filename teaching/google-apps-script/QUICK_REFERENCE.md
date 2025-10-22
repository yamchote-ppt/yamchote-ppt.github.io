# Quick Reference Guide
## Google Apps Script Setup for Quiz System

This is a condensed version for quick deployment. See DEPLOYMENT_GUIDE.md for detailed instructions.

---

## ⚡ Quick Setup (10 Minutes)

### 1️⃣ Create Spreadsheet
1. Go to [sheets.google.com](https://sheets.google.com)
2. Create new spreadsheet: **"819605 Quiz Submissions"**
3. Copy the Spreadsheet ID from URL
4. Create 3 sheets: `QuizData`, `Submissions`, `Log`

### 2️⃣ Add Sample Data to QuizData Sheet

**Headers (Row 1):**
```
QuizID | QuestionID | Question | Type | Options | CorrectAnswer | Points | Explanation
```

**Sample Row:**
```
demo | q1 | What is 2 + 2? | multiple-choice | ["2", "3", "4", "5"] | 2 | 10 | Basic math
```

### 3️⃣ Deploy Apps Script
1. Extensions → Apps Script
2. Paste `Code.gs` content
3. Update line 17: `SPREADSHEET_ID: 'YOUR_ID_HERE'`
4. Save (Ctrl+S)
5. Run `testSetup()` and authorize
6. Deploy → New deployment → Web app
7. Who has access: **Anyone**
8. Click Deploy and **copy the URL**

### 4️⃣ Update Quiz Config
In `assets/js/quiz-config.js`:
```javascript
APP_SCRIPT_URL: 'https://script.google.com/macros/s/AKfycby.../exec'
```

### 5️⃣ Test
1. Open quiz in browser
2. Submit a test answer
3. Check `Submissions` sheet for new row

---

## 📋 Sheet Structures Cheat Sheet

### QuizData Columns
```
A: QuizID       → "demo", "quiz1", "midterm"
B: QuestionID   → "q1", "q2", "q3"
C: Question     → "What is 2 + 2?"
D: Type         → "multiple-choice" or "text"
E: Options      → ["Option 1", "Option 2"]
F: CorrectAnswer → 0, 1, 2 (index of correct option)
G: Points       → 10
H: Explanation  → "Explanation text"
```

### Submissions Columns (Auto-created)
```
SubmissionID | Timestamp | StudentID | StudentName | QuizID | 
QuizTitle | Score | TotalPoints | Percentage | Grade | 
TimeUsedSec | TabSwitchCount | UserAgent | ClientScore | 
ClientGrade | Answers (JSON)
```

---

## 🔧 Common Issues

| Problem | Solution |
|---------|----------|
| "Script not found" | Make sure you deployed as Web App |
| "Authorization required" | Run testSetup() and approve permissions |
| "Cannot find spreadsheet" | Check SPREADSHEET_ID in Code.gs |
| No data in Submissions | Check Log sheet for errors |
| Wrong scores | QuizData CorrectAnswer must match question options |

---

## 🎯 Testing Checklist

- [ ] testSetup() runs without errors
- [ ] QuizData has at least one quiz with questions
- [ ] Web App deployed with "Anyone" access
- [ ] APP_SCRIPT_URL updated in quiz-config.js
- [ ] Test submission appears in Submissions sheet
- [ ] Scores calculated correctly
- [ ] No errors in Log sheet

---

## 📞 Key Functions

### In Apps Script Editor

**Test Connection:**
```javascript
testSetup()  // Run this first
```

**Create Sample Data:**
```javascript
createSampleQuizData()  // Populates QuizData sheet
```

**Manual Test Submission:**
```javascript
// Create test payload and call doPost()
```

---

## 🔐 Security Settings

- **Execute as:** Me (your account)
- **Who has access:** Anyone
- ⚠️ Anyone can submit, but server validates all data
- Results only visible to spreadsheet editors

---

## 📊 Data Flow

```
Student Submits → ResultsSaver.save() 
                → POST to Apps Script URL
                → doPost() receives data
                → validateSubmission()
                → loadQuizData() from QuizData sheet
                → gradeSubmission() (server-side)
                → saveSubmission() to Submissions sheet
                → Return server-calculated scores
```

---

## 🔄 Update Deployed Script

1. Edit Code.gs in Apps Script editor
2. Save changes
3. Deploy → Manage deployments
4. Edit existing deployment (pencil icon)
5. Version: New version
6. Deploy
7. ✅ URL stays the same - no config update needed

---

## 📈 Quick Analytics

### In Google Sheets:

**Average score for a quiz:**
```
=AVERAGEIF(Submissions!E:E, "quiz1", Submissions!I:I)
```

**Count of each grade:**
```
=COUNTIF(Submissions!J:J, "A")
```

**Students with high tab switches:**
```
=FILTER(Submissions!C:D, Submissions!L:L > 5)
```

---

## 💡 Pro Tips

1. **Test with sample data first** before adding real questions
2. **Back up your spreadsheet** regularly (File → Download)
3. **Use the Log sheet** to debug issues
4. **Index starts at 0** for CorrectAnswer (0 = first option)
5. **Options must be JSON** with double quotes: `["A", "B", "C"]`
6. **Keep spreadsheet private** - contains student grades
7. **Server score is authoritative** - client score is for reference only

---

## 📱 Mobile Testing

The quiz system works on mobile, but testing submissions:
1. Open quiz on phone browser
2. Complete and submit
3. Check Submissions sheet on desktop
4. Verify mobile UserAgent in column M

---

## 🎓 Ready to Go Live?

Final checklist:
- [ ] All quiz questions added to QuizData
- [ ] CorrectAnswer values verified
- [ ] Apps Script deployed and URL in config
- [ ] Test submission successful
- [ ] Spreadsheet permissions set correctly
- [ ] Backup created
- [ ] Announcement sent to students

---

**Need more details?** See `DEPLOYMENT_GUIDE.md`

**Sheet structure details?** See `SPREADSHEET_TEMPLATE.md`

**Good luck with your quiz! 🎉**
