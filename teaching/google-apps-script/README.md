# Google Apps Script for Quiz System
## 819605 - Discrete Mathematics | Southeast Asia University

This folder contains the Google Apps Script backend for the quiz submission system.

---

## 📁 Files in This Folder

| File | Purpose |
|------|---------|
| **Code.gs** | Main Apps Script code - handles quiz submissions, grading, and data storage |
| **DEPLOYMENT_GUIDE.md** | Detailed step-by-step deployment instructions (START HERE) |
| **SPREADSHEET_TEMPLATE.md** | Google Sheets structure and data format documentation |
| **QUICK_REFERENCE.md** | Quick setup guide and troubleshooting tips |
| **README.md** | This file - overview and getting started |

---

## 🚀 Getting Started

### First Time Setup

1. **Read the deployment guide first:**
   ```
   📖 Start with: DEPLOYMENT_GUIDE.md
   ```

2. **Create your Google Spreadsheet** with three sheets:
   - `QuizData` - Store questions and answers
   - `Submissions` - Store student submissions (auto-created)
   - `Log` - Activity logs (auto-created)

3. **Deploy the script:**
   - Copy `Code.gs` to Apps Script editor
   - Update SPREADSHEET_ID
   - Deploy as Web App
   - Copy the deployment URL

4. **Update your quiz config:**
   - Edit `assets/js/quiz-config.js`
   - Set APP_SCRIPT_URL to your deployment URL

5. **Test the integration:**
   - Submit a test quiz
   - Verify data in Submissions sheet

### Quick Setup (If You Know What You're Doing)

```
📖 Use: QUICK_REFERENCE.md
```

---

## 🎯 What This Script Does

### Receives Quiz Submissions
- Accepts POST requests from `ResultsSaver.save()` in the quiz system
- Validates student information and submission data
- Logs all activity and errors

### Server-Side Grading
- Loads correct answers from `QuizData` sheet
- Grades each answer independently
- Calculates total score, percentage, and letter grade
- **Server grade is authoritative** - protects against client-side tampering

### Data Storage
- Saves all submissions to `Submissions` sheet
- Stores detailed answer data in JSON format
- Captures anti-cheat metrics (tab switches, time used)
- Maintains audit trail with timestamps

### Returns Results
- Sends server-calculated scores back to client
- Updates quiz results screen with verified grades
- Provides submission confirmation

---

## 📊 Data Flow Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    Quiz System (Web)                     │
│  Student completes quiz → ResultsSaver.save() called    │
└──────────────────────────┬──────────────────────────────┘
                           │
                           │ POST request with:
                           │ - Student info
                           │ - Quiz ID
                           │ - Answers array
                           │ - Anti-cheat data
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│              Google Apps Script (Code.gs)                │
│                                                          │
│  1. doPost() receives request                           │
│  2. validateSubmission() checks data                    │
│  3. loadQuizData() fetches correct answers              │
│  4. gradeSubmission() calculates score                  │
│  5. saveSubmission() stores in Sheets                   │
│  6. Return server-calculated results                    │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│                  Google Sheets Database                  │
│                                                          │
│  • QuizData: Questions & correct answers                │
│  • Submissions: Student results (NEW ROW)               │
│  • Log: Activity and error logs                         │
└─────────────────────────────────────────────────────────┘
                           │
                           │ Response with:
                           │ - Server-calculated score
                           │ - Grade
                           │ - Submission ID
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│              Quiz System Updates Results                 │
│  Display server-verified score and grade to student     │
└─────────────────────────────────────────────────────────┘
```

---

## 🔒 Security Features

### Server-Side Validation
✅ All grading happens on the server
✅ Client-calculated scores are logged but not trusted
✅ Correct answers never sent to client
✅ Question data fetched from secure spreadsheet

### Data Integrity
✅ Student ID format validation
✅ Quiz ID verification
✅ Answer count validation
✅ Duplicate submission detection (via unique IDs)

### Audit Trail
✅ All submissions logged with timestamp
✅ Anti-cheat metrics captured (tab switches, time)
✅ User agent and client metadata stored
✅ Error logging for troubleshooting

### Privacy
✅ Spreadsheet only accessible to instructors
✅ Students cannot view others' results
✅ Apps Script runs under instructor's permissions

---

## 🧪 Testing

### Test Functions Available

Run these from the Apps Script editor:

1. **`testSetup()`**
   - Verifies spreadsheet connection
   - Tests quiz data loading
   - Checks sheet structure
   - **Run this first!**

2. **`createSampleQuizData()`**
   - Populates QuizData with sample questions
   - Useful for initial testing
   - Creates "demo" quiz with 3 questions

### Manual Testing Steps

1. Run `testSetup()` - should pass all checks
2. Add questions to QuizData sheet
3. Open quiz system in browser
4. Submit a test quiz
5. Check Submissions sheet for new row
6. Verify score calculation is correct
7. Check Log sheet for any errors

---

## 📝 Maintenance

### Regular Tasks

**Weekly:**
- Review Log sheet for errors
- Check submission counts
- Verify no anomalies

**After Each Quiz:**
- Export results for gradebook
- Review anti-cheat metrics
- Archive old data

**Semester End:**
- Back up entire spreadsheet
- Export all data to CSV
- Archive for records
- Clear for next semester

### Updating the Script

1. Make changes in Apps Script editor
2. Save the file
3. Deploy → Manage deployments
4. Edit deployment → New version
5. Deploy (URL stays the same)

---

## 🐛 Troubleshooting

### Common Issues

| Symptom | Cause | Solution |
|---------|-------|----------|
| "Script not found" | Not deployed as Web App | Deploy → New deployment → Web app |
| "Authorization required" | Permissions not granted | Run testSetup() and approve |
| "Cannot find spreadsheet" | Wrong SPREADSHEET_ID | Check ID in Code.gs line 17 |
| No data in Submissions | Validation failed | Check Log sheet for errors |
| Wrong scores | Incorrect CorrectAnswer values | Verify indices in QuizData (0-based) |
| CORS errors | Wrong access level | Deploy with "Anyone" access |

### Debug Steps

1. Check `Log` sheet first
2. Run `testSetup()` in Apps Script
3. View Executions (Apps Script → Executions)
4. Test with sample data
5. Verify QuizData format
6. Check browser console for network errors

---

## 📚 API Reference

### POST Request Format

The quiz system sends this to your Apps Script:

```javascript
{
  "studentId": "6501234567",
  "studentName": "John Doe",
  "quizId": "quiz1",
  "quizTitle": "Quiz 1: Set Theory",
  "timeUsedSec": 1234,
  "answers": [
    {
      "questionId": "q1",
      "userAnswer": 2
    },
    {
      "questionId": "q2",
      "userAnswer": 0
    }
  ],
  "clientMeta": {
    "clientReported": {
      "score": 10,
      "totalPoints": 20,
      "percentage": 50,
      "grade": "F"
    },
    "tabSwitchCount": 0,
    "userAgent": "Mozilla/5.0..."
  }
}
```

### Response Format

Apps Script returns:

```javascript
{
  "ok": true,
  "message": "Submission successful",
  "computed": {
    "correct": 1,
    "incorrect": 1,
    "score": 10,
    "totalPoints": 20,
    "percentage": 50,
    "grade": "F"
  },
  "submissionId": "abc-123-def-456",
  "timestamp": "2025-10-16T10:30:00.000Z"
}
```

---

## 🔗 Integration Points

### Frontend (ResultsSaver class)
- Sends POST request to APP_SCRIPT_URL
- Includes student info, answers, and metadata
- Receives server-calculated results
- Updates UI with verified scores

### Backend (Code.gs)
- Receives and validates submissions
- Loads correct answers from QuizData
- Performs authoritative grading
- Stores results in Submissions sheet
- Returns verified scores

### Database (Google Sheets)
- QuizData: Question bank
- Submissions: Student results
- Log: Activity and errors

---

## 📦 Dependencies

### Required Google Services
- Google Sheets API (automatic)
- Google Apps Script runtime
- SpreadsheetApp service
- ContentService for JSON responses
- Utilities for UUID generation

### No External Libraries
- All code is pure Apps Script
- No npm packages needed
- No API keys required
- Runs entirely on Google infrastructure

---

## 🌟 Features

✅ **Server-side grading** - Prevents cheating
✅ **Automatic validation** - Checks all inputs
✅ **Detailed logging** - Easy debugging
✅ **JSON storage** - Flexible answer formats
✅ **Anti-cheat tracking** - Tab switches logged
✅ **UUID submissions** - Unique IDs for each attempt
✅ **Error handling** - Graceful failure recovery
✅ **Sample data generator** - Easy testing

---

## 🎓 Academic Integrity

This system includes several features to promote academic integrity:

1. **Server-side grading** - Students cannot modify scores
2. **Tab switch detection** - Warns against looking up answers
3. **Time tracking** - Identifies unusually fast/slow submissions
4. **Submission logging** - Complete audit trail
5. **Browser fingerprinting** - UserAgent captured

**Note:** These are deterrents, not foolproof. Use in combination with other academic integrity measures.

---

## 📞 Support

### For Issues:
1. Check the Log sheet
2. Review DEPLOYMENT_GUIDE.md
3. Run testSetup() function
4. Check Executions log in Apps Script
5. Verify spreadsheet structure

### For Customization:
- Modify grading thresholds in CONFIG section
- Add email notifications in saveSubmission()
- Implement additional validation rules
- Export results to other formats

---

## 📄 License

This script is part of the 819605 Discrete Mathematics course materials at Southeast Asia University. Modify and adapt as needed for your institution.

---

## ✅ Quick Start Checklist

- [ ] Read DEPLOYMENT_GUIDE.md
- [ ] Create Google Spreadsheet
- [ ] Add QuizData, Submissions, Log sheets
- [ ] Copy Code.gs to Apps Script
- [ ] Update SPREADSHEET_ID
- [ ] Run testSetup() and authorize
- [ ] Add sample questions
- [ ] Deploy as Web App
- [ ] Copy deployment URL
- [ ] Update quiz-config.js
- [ ] Test submission
- [ ] Verify in Submissions sheet

---

**Ready to deploy? Start with `DEPLOYMENT_GUIDE.md`! 🚀**
