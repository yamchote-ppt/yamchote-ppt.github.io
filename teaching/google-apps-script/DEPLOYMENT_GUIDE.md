# Google Apps Script Deployment Guide
## Quiz Result Submission Handler for 819605 - Discrete Mathematics

This guide will walk you through deploying the `Code.gs` script to Google Apps Script and connecting it to your quiz system.

---

## 📋 Prerequisites

- Google Account with access to Google Drive and Google Sheets
- The quiz system HTML files deployed on a web server
- Basic understanding of Google Apps Script

---

## 🚀 Step-by-Step Deployment

### Step 1: Create a Google Spreadsheet

1. Go to [Google Sheets](https://sheets.google.com)
2. Click **"+ Blank"** to create a new spreadsheet
3. Rename it to: **"819605 Quiz Submissions"**
4. Note the **Spreadsheet ID** from the URL:
   ```
   https://docs.google.com/spreadsheets/d/[SPREADSHEET_ID_HERE]/edit
   ```
5. Copy this ID - you'll need it in Step 4

### Step 2: Create Required Sheets

Create three sheets in your spreadsheet with these exact names:

#### Sheet 1: `QuizData`
- This stores quiz questions and correct answers
- Columns:
  - **QuizID** - Quiz identifier (e.g., "demo", "quiz1", "midterm")
  - **QuestionID** - Unique question ID (e.g., "q1", "q2")
  - **Question** - The question text
  - **Type** - Question type: "multiple-choice" or "text"
  - **Options** - JSON array of options: `["Option A", "Option B", "Option C", "Option D"]`
  - **CorrectAnswer** - Index of correct answer (0-based) for multiple choice
  - **Points** - Points awarded for correct answer
  - **Explanation** - Optional explanation text

**Example data:**
| QuizID | QuestionID | Question | Type | Options | CorrectAnswer | Points | Explanation |
|--------|------------|----------|------|---------|---------------|--------|-------------|
| demo | q1 | What is 2 + 2? | multiple-choice | ["2", "3", "4", "5"] | 2 | 10 | Basic arithmetic |
| demo | q2 | Capital of Thailand? | multiple-choice | ["Bangkok", "Chiang Mai", "Phuket"] | 0 | 10 | Geography |

#### Sheet 2: `Submissions`
- This will store student submissions (auto-created by script)
- Leave this sheet empty - the script will create headers automatically

#### Sheet 3: `Log`
- This will store activity and error logs (auto-created by script)
- Leave this sheet empty - the script will create headers automatically

### Step 3: Open Apps Script Editor

1. In your Google Sheet, click **Extensions** → **Apps Script**
2. This opens the Apps Script editor in a new tab
3. Delete any existing code in `Code.gs`

### Step 4: Add the Script Code

1. Copy the entire contents of `Code.gs` from the `google-apps-script` folder
2. Paste it into the Apps Script editor
3. **Important:** Update the `SPREADSHEET_ID` in the CONFIG section:
   ```javascript
   const CONFIG = {
     SPREADSHEET_ID: 'YOUR_SPREADSHEET_ID_HERE', // Replace with your actual ID from Step 1
     // ... rest of config
   };
   ```
4. Click the **Save** icon (💾) or press `Ctrl+S`
5. Name your project: **"Quiz Submission Handler"**

### Step 5: Test the Setup

1. In the Apps Script editor, select the function dropdown (top center)
2. Choose **`testSetup`** from the dropdown
3. Click **Run** (▶️ icon)
4. **First time only:** You'll need to authorize the script:
   - Click **Review Permissions**
   - Choose your Google account
   - Click **Advanced** → **Go to Quiz Submission Handler (unsafe)**
   - Click **Allow**
5. Check the **Execution log** (bottom panel) - you should see:
   ```
   ✓ Spreadsheet access OK
   ✓ Quiz data loading OK
   Test complete!
   ```

### Step 6: Create Sample Quiz Data (Optional)

To populate the QuizData sheet with sample questions:

1. In the function dropdown, select **`createSampleQuizData`**
2. Click **Run** (▶️)
3. Check the `QuizData` sheet - it should now have sample questions

### Step 7: Deploy as Web App

1. Click **Deploy** → **New deployment**
2. Click the gear icon ⚙️ next to "Select type"
3. Choose **Web app**
4. Configure deployment settings:
   - **Description:** "Quiz Submission API v1"
   - **Execute as:** Me (your email)
   - **Who has access:** Anyone
     - ⚠️ **Important:** Must be "Anyone" for the quiz system to access it
5. Click **Deploy**
6. **Copy the Web App URL** - it will look like:
   ```
   https://script.google.com/macros/s/AKfycby.../exec
   ```

### Step 8: Update Quiz Configuration

1. Open `assets/js/quiz-config.js` in your project
2. Update the `APP_SCRIPT_URL` with the URL from Step 7:
   ```javascript
   const CONFIG = {
       APP_SCRIPT_URL: 'https://script.google.com/macros/s/AKfycby.../exec',
       // ... rest of config
   };
   ```
3. Save the file
4. Re-upload to your web server

---

## 🧪 Testing the Integration

### Test 1: Submit a Demo Quiz

1. Open your quiz system in a web browser
2. Fill in student information:
   - Student ID: `6501234567`
   - Name: `Test Student`
   - Select: `Demo Quiz`
3. Complete the quiz and submit
4. Check the `Submissions` sheet - you should see a new row with:
   - Student information
   - Score and grade (server-calculated)
   - Timestamp
   - Answers in JSON format

### Test 2: Verify Server-Side Grading

1. Submit the same quiz twice with different answers
2. Compare the scores in the `Submissions` sheet
3. Verify that the grade matches the scoring logic:
   - A: ≥80%
   - B: ≥70%
   - C: ≥60%
   - D: ≥50%
   - F: <50%

### Test 3: Check Error Logging

1. Try submitting with invalid data (e.g., empty student ID)
2. Check the `Log` sheet for error entries
3. Errors should be logged with timestamps and details

---

## 🔧 Troubleshooting

### Problem: "Script function not found: doPost"
**Solution:** Make sure you saved the script and deployed it as a Web App (Step 7)

### Problem: "Authorization required" error
**Solution:** Re-run the authorization process in Step 5

### Problem: "Cannot find spreadsheet" error
**Solution:** 
- Verify the SPREADSHEET_ID in Code.gs matches your actual spreadsheet ID
- Check that you have edit access to the spreadsheet

### Problem: Quiz submissions not appearing in sheet
**Solution:**
- Check the `Log` sheet for error messages
- Verify the Web App URL in `quiz-config.js` is correct
- Ensure the Web App is deployed with "Anyone" access
- Check browser console for network errors

### Problem: Scores don't match between client and server
**Solution:** This is normal - the server performs authoritative grading. The `Submissions` sheet shows the correct scores.

---

## 📊 Understanding the Data Flow

```
┌─────────────────┐
│  Quiz System    │
│  (Browser)      │
└────────┬────────┘
         │ 1. Student submits quiz
         │
         ▼
┌─────────────────┐
│  ResultsSaver   │
│  (quiz-system.js)│
└────────┬────────┘
         │ 2. POST request with answers
         │
         ▼
┌─────────────────┐
│  Code.gs        │
│  (Apps Script)  │
└────────┬────────┘
         │ 3. Validate & grade
         │ 4. Load correct answers from QuizData
         │ 5. Calculate score
         │
         ▼
┌─────────────────┐
│  Google Sheets  │
│  (Submissions)  │
└─────────────────┘
```

---

## 🔒 Security Considerations

### Current Setup (Development)
- ✅ Server-side validation and grading
- ✅ Activity logging
- ✅ Anti-cheat metrics captured
- ⚠️ Anyone can submit (required for web app)

### Production Recommendations
1. **Add authentication:**
   - Implement a shared secret key
   - Add JWT tokens for requests
   - Validate request origin

2. **Rate limiting:**
   - Add submission throttling per student
   - Prevent duplicate submissions

3. **Enhanced validation:**
   - Verify student ID against enrollment database
   - Check submission time windows
   - Validate quiz availability

---

## 🔄 Updating the Script

When you need to make changes:

1. Edit `Code.gs` in the Apps Script editor
2. Click **Save**
3. Click **Deploy** → **Manage deployments**
4. Click the edit icon (pencil) next to your deployment
5. Under "Version", select **New version**
6. Add a description (e.g., "v2 - Added new validation")
7. Click **Deploy**
8. **Note:** The Web App URL stays the same - no need to update `quiz-config.js`

---

## 📈 Advanced Features

### Export Results to CSV
Add this function to export all submissions:

```javascript
function exportSubmissionsToCSV() {
  const ss = SpreadsheetApp.openById(CONFIG.SPREADSHEET_ID);
  const sheet = ss.getSheetByName(CONFIG.SHEETS.SUBMISSIONS);
  const data = sheet.getDataRange().getValues();
  
  // Convert to CSV and download
  // Implementation details...
}
```

### Send Email Notifications
Add this to notify instructors of new submissions:

```javascript
function sendSubmissionNotification(submission) {
  MailApp.sendEmail({
    to: 'instructor@university.edu',
    subject: 'New Quiz Submission: ' + submission.studentName,
    body: 'Student ' + submission.studentName + ' completed ' + submission.quizTitle
  });
}
```

### Generate Reports
Create a function to analyze submission data:

```javascript
function generateQuizReport(quizId) {
  // Calculate average score, grade distribution, etc.
  // Implementation details...
}
```

---

## 📞 Support

If you encounter issues:

1. Check the `Log` sheet for error messages
2. Review the Apps Script execution logs (View → Executions)
3. Test the `testSetup()` function
4. Verify all configuration settings

---

## ✅ Deployment Checklist

- [ ] Created Google Spreadsheet
- [ ] Noted Spreadsheet ID
- [ ] Created three sheets: QuizData, Submissions, Log
- [ ] Added quiz questions to QuizData sheet
- [ ] Opened Apps Script editor
- [ ] Pasted Code.gs and updated SPREADSHEET_ID
- [ ] Saved and named the project
- [ ] Ran testSetup() and authorized permissions
- [ ] Created sample data (optional)
- [ ] Deployed as Web App with "Anyone" access
- [ ] Copied Web App URL
- [ ] Updated quiz-config.js with Web App URL
- [ ] Tested submission flow
- [ ] Verified data in Submissions sheet
- [ ] Checked Log sheet for any errors

---

**Congratulations! Your quiz submission system is now live! 🎉**
