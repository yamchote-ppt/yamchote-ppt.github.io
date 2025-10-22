# Google Sheets Template Structure
## Quiz Submission System - 819605 Discrete Mathematics

This document describes the structure of Google Sheets used by the quiz submission system.

---

## 📊 Sheet 1: QuizData

**Purpose:** Stores quiz questions, answer options, and correct answers

### Column Structure

| Column | Name | Type | Description | Example |
|--------|------|------|-------------|---------|
| A | QuizID | String | Unique quiz identifier | `demo`, `quiz1`, `midterm`, `final` |
| B | QuestionID | String | Unique question identifier | `q1`, `q2`, `q3` |
| C | Question | Text | The question text (can include HTML) | `What is 2 + 2?` |
| D | Type | String | Question type | `multiple-choice` or `text` |
| E | Options | JSON Array | Answer options (for multiple-choice) | `["2", "3", "4", "5"]` |
| F | CorrectAnswer | Number/String | Index of correct answer (0-based) | `2` (means 3rd option) |
| G | Points | Number | Points awarded for correct answer | `10` |
| H | Explanation | Text | Optional explanation (shown after submission) | `4 is the correct answer` |

### Example Data

```
QuizID | QuestionID | Question                          | Type            | Options                                | CorrectAnswer | Points | Explanation
-------|------------|-----------------------------------|-----------------|----------------------------------------|---------------|--------|------------------
demo   | q1         | What is 2 + 2?                    | multiple-choice | ["2", "3", "4", "5"]                  | 2             | 10     | Basic arithmetic
demo   | q2         | What is the capital of Thailand?  | multiple-choice | ["Bangkok", "Chiang Mai", "Phuket"]   | 0             | 10     | Geography
quiz1  | q1         | What is a set?                    | multiple-choice | ["A collection", "A number", "A graph"] | 0           | 5      | Set theory basics
quiz1  | q2         | Is {1,2} ⊆ {1,2,3}?              | multiple-choice | ["True", "False"]                      | 0             | 5      | Subset definition
```

### Notes
- **QuizID** must match the `value` in the quiz selection dropdown in your HTML
- **QuestionID** should be unique within each quiz
- **Options** must be valid JSON array format with double quotes
- **CorrectAnswer** is 0-based index (0 = first option, 1 = second, etc.)
- For **text** type questions, set CorrectAnswer to the expected text (case-sensitive)

---

## 📊 Sheet 2: Submissions

**Purpose:** Stores all student quiz submissions with server-calculated scores

### Column Structure

| Column | Name | Type | Description |
|--------|------|------|-------------|
| A | SubmissionID | UUID | Unique identifier for this submission |
| B | Timestamp | ISO DateTime | When the submission was received |
| C | StudentID | String | Student identification number |
| D | StudentName | String | Student full name |
| E | QuizID | String | Which quiz was taken |
| F | QuizTitle | String | Quiz display name |
| G | Score | Number | Points earned (server-calculated) |
| H | TotalPoints | Number | Maximum possible points |
| I | Percentage | Number | Score percentage (0-100) |
| J | Grade | String | Letter grade (A, B, C, D, F) |
| K | TimeUsedSec | Number | Time taken to complete (seconds) |
| L | TabSwitchCount | Number | Number of times student left the page |
| M | UserAgent | String | Browser information |
| N | ClientScore | Number | Score calculated by client (for comparison) |
| O | ClientGrade | String | Grade calculated by client |
| P | Answers (JSON) | JSON | Detailed answers with grading |

### Example Data

```
SubmissionID | Timestamp           | StudentID  | StudentName  | QuizID | QuizTitle | Score | TotalPoints | Percentage | Grade
-------------|---------------------|------------|--------------|--------|-----------|-------|-------------|------------|------
abc123...    | 2025-10-16T10:30:00 | 6501234567 | John Doe     | demo   | Demo Quiz | 20    | 30          | 67         | C
def456...    | 2025-10-16T11:45:00 | 6501234568 | Jane Smith   | quiz1  | Quiz 1    | 45    | 50          | 90         | A
```

### Answers JSON Format

The Answers column contains detailed grading information:

```json
[
  {
    "questionId": "q1",
    "userAnswer": 2,
    "correctAnswer": 2,
    "isCorrect": true,
    "pointsEarned": 10,
    "pointsPossible": 10
  },
  {
    "questionId": "q2",
    "userAnswer": 1,
    "correctAnswer": 0,
    "isCorrect": false,
    "pointsEarned": 0,
    "pointsPossible": 10
  }
]
```

---

## 📊 Sheet 3: Log

**Purpose:** Activity and error logging for debugging and monitoring

### Column Structure

| Column | Name | Type | Description |
|--------|------|------|-------------|
| A | Timestamp | ISO DateTime | When the event occurred |
| B | Type | String | Event type: `INFO`, `ERROR`, `WARNING` |
| C | Message | String | Short description of the event |
| D | Details | JSON/String | Additional details or error stack trace |

### Example Data

```
Timestamp           | Type  | Message                    | Details
--------------------|-------|----------------------------|----------------------------------
2025-10-16T10:30:00 | INFO  | Submission received        | {"studentId": "6501234567"}
2025-10-16T10:30:05 | ERROR | Quiz data loading failed   | Error: Sheet not found...
2025-10-16T11:00:00 | INFO  | New deployment activated   | {"version": "v1.2"}
```

---

## 🔧 Setup Instructions

### Creating the Spreadsheet from Scratch

1. **Create new Google Sheet:**
   - Go to sheets.google.com
   - Click "+ Blank"
   - Rename to "819605 Quiz Submissions"

2. **Create Sheet 1 - QuizData:**
   - Rename "Sheet1" to "QuizData"
   - Add header row with columns A-H as shown above
   - Format column E (Options) as plain text (Format → Number → Plain text)
   - Add your quiz questions

3. **Create Sheet 2 - Submissions:**
   - Click "+" to add new sheet
   - Rename to "Submissions"
   - Leave empty (script will auto-create headers)

4. **Create Sheet 3 - Log:**
   - Click "+" to add new sheet
   - Rename to "Log"
   - Leave empty (script will auto-create headers)

### Using the Sample Data Generator

Instead of manually creating data, you can run the `createSampleQuizData()` function in Apps Script:

1. Open Apps Script editor (Extensions → Apps Script)
2. Add the Code.gs file
3. Run the function `createSampleQuizData()`
4. Check the QuizData sheet - it will have sample questions

---

## 📝 Data Entry Tips

### Adding Multiple-Choice Questions

1. Write question text in Column C
2. In Column E (Options), enter as JSON array:
   ```
   ["Option A", "Option B", "Option C", "Option D"]
   ```
3. Count which option is correct (starting from 0)
4. Enter the index in Column F

**Example:**
- Options: `["Apple", "Banana", "Orange"]`
- Correct answer is "Orange"
- Enter `2` in CorrectAnswer (0=Apple, 1=Banana, 2=Orange)

### Special Characters in Questions

You can use HTML in question text:
```html
Is {1,2,3} ⊆ {1,2,3,4}?
<br><strong>Hint:</strong> Think about subsets!
```

### Mathematical Notation

For mathematical symbols, you can use:
- Unicode: ∪ ∩ ⊆ ⊇ ∈ ∅ ℕ ℤ ℝ
- HTML entities: `&cup;` `&cap;` `&sube;`
- LaTeX (if implementing MathJax): `$x^2 + y^2 = z^2$`

---

## 📊 Data Analysis Queries

### Get Average Score by Quiz

```javascript
=AVERAGEIF(Submissions!E:E, "quiz1", Submissions!I:I)
```

### Count Submissions by Grade

```javascript
=COUNTIF(Submissions!J:J, "A")
```

### Find Students Who Haven't Submitted

Use VLOOKUP or QUERY to compare enrollment list with submissions.

### Grade Distribution Chart

1. Select Submissions sheet
2. Insert → Chart
3. Chart type: Column chart
4. X-axis: Grade column (J)
5. Count values

---

## 🔒 Permissions and Sharing

### For Production Use:

1. **Quiz Data Sheet:**
   - Instructor: Editor
   - TAs: Editor or Viewer
   - Students: No access

2. **Submissions Sheet:**
   - Instructor: Editor
   - TAs: Viewer
   - Students: No access

3. **Apps Script:**
   - Only instructor should have edit access
   - Deploy as "Execute as: Me" and "Who has access: Anyone"

### Privacy Considerations:

- Submissions sheet contains student grades - keep private
- Never share the spreadsheet URL publicly
- Use Apps Script for data access only
- Consider encrypting sensitive data

---

## 📦 Backup and Export

### Manual Backup

1. File → Download → Microsoft Excel (.xlsx)
2. Save with timestamp: `quiz-submissions-2025-10-16.xlsx`

### Automated Backup (Apps Script)

Add this function to create daily backups:

```javascript
function createDailyBackup() {
  var ss = SpreadsheetApp.openById(CONFIG.SPREADSHEET_ID);
  var destFolder = DriveApp.getFolderById('YOUR_BACKUP_FOLDER_ID');
  var date = Utilities.formatDate(new Date(), 'GMT+7', 'yyyy-MM-dd');
  ss.copy('Quiz Submissions Backup ' + date).moveTo(destFolder);
}
```

Set up a time-driven trigger to run this daily.

---

## 🔄 Maintenance Tasks

### Weekly:
- [ ] Review Log sheet for errors
- [ ] Check submission counts match expected
- [ ] Verify no duplicate submissions
- [ ] Back up spreadsheet

### After Each Quiz:
- [ ] Export results for gradebook
- [ ] Review any anomalies (very high/low tab switches)
- [ ] Check for potential cheating indicators
- [ ] Archive old submissions

### Semester End:
- [ ] Export all data to CSV
- [ ] Create final grade report
- [ ] Archive entire spreadsheet
- [ ] Clear data for next semester

---

## 📞 Support

For issues with spreadsheet structure or data:
1. Check column names match exactly (case-sensitive)
2. Verify JSON format in Options column
3. Ensure CorrectAnswer indices are correct
4. Review Log sheet for error messages
5. Test with sample data first

---

**Note:** Keep this spreadsheet and its URL private to protect student data!
