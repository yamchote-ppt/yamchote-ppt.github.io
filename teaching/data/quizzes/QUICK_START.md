# Quick Start Guide - Adding Your First Quiz

## ⚡ 5-Minute Setup

### Step 1: Copy the Template (1 min)

```bash
# Navigate to the quizzes directory
cd teaching/data/quizzes/

# Copy the template
cp TEMPLATE-quiz.json 819605-myquiz.json
```

Or manually:
1. Open `TEMPLATE-quiz.json`
2. Copy all content
3. Create new file `819605-myquiz.json`
4. Paste content

### Step 2: Edit Your Quiz (2 min)

Open `819605-myquiz.json` and change:

```json
{
  "id": "myquiz",                    ← Change this
  "courseCode": "819605",            ← Your course code
  "title": "My First Quiz",          ← Quiz title
  "duration": 30,                     ← Time in minutes
  "questions": [
    {
      "id": 1,
      "question": "What is 2+2?",    ← Your question
      "type": "multiple-choice",
      "points": 10,
      "options": ["3", "4", "5", "6"],
      "correctAnswer": 1              ← Index of "4" (0-based: 0,1,2,3)
    }
  ]
}
```

**Remove these lines** (they're just comments):
- Any line starting with `_comment`
- Any line starting with `_note`
- The `_instructions` section

### Step 3: Register Your Quiz (1 min)

Open `quiz-config.json` and add:

```json
{
  "courses": {
    "819605": {
      "quizzes": [
        {
          "id": "myquiz",                          ← Same as in quiz file
          "file": "819605-myquiz.json",            ← Your quiz filename
          "displayName": "My First Quiz",          ← Shown in dropdown
          "enabled": true                           ← Set to true
        }
      ]
    }
  }
}
```

### Step 4: Test It! (1 min)

1. Open `819605-2-2568-demo.html` in browser
2. Select your quiz from dropdown
3. Click "เริ่มทำข้อสอบ"
4. Verify questions appear correctly

## 🎯 Common Tasks

### Add Multiple Choice Question

```json
{
  "id": 2,
  "question": "Which is correct?",
  "type": "multiple-choice",
  "points": 10,
  "options": ["A", "B", "C", "D"],
  "correctAnswer": 2
}
```

### Add Essay/Text Question

```json
{
  "id": 3,
  "question": "Explain your answer.",
  "type": "text",
  "points": 20,
  "correctAnswer": "Sample answer for grading reference"
}
```

### Change Time Limit

```json
{
  "duration": 45
}
```

### Disable a Quiz Temporarily

In `quiz-config.json`:

```json
{
  "enabled": false
}
```

## ⚠️ Common Mistakes

❌ **Wrong:**
```json
"correctAnswer": "1"    // String instead of number
```

✅ **Correct:**
```json
"correctAnswer": 1      // Number (for multiple choice)
```

---

❌ **Wrong:**
```json
"correctAnswer": 4      // Index 4 doesn't exist (only 0-3 for 4 options)
```

✅ **Correct:**
```json
"correctAnswer": 3      // Use 0, 1, 2, or 3 for 4 options
```

---

❌ **Wrong:**
```json
"duration": "30"        // String instead of number
```

✅ **Correct:**
```json
"duration": 30          // Number without quotes
```

---

❌ **Wrong:**
```json
{
  "id": "quiz1",
  "file": "819605-myquiz.json",  // ID doesn't match filename
  ...
}
```

✅ **Correct:**
```json
{
  "id": "myquiz",                 // Matches quiz file ID
  "file": "819605-myquiz.json",
  ...
}
```

## 🔍 Validation Checklist

Before deploying your quiz:

- [ ] All question IDs are unique and sequential
- [ ] `correctAnswer` values are valid (0-3 for 4 options)
- [ ] No trailing commas in JSON
- [ ] Quiz `id` matches in both files
- [ ] `enabled: true` in config
- [ ] File saved in `data/quizzes/` directory
- [ ] Tested in browser (hard refresh: Ctrl+F5)

## 🛠️ JSON Validation Tools

Test your JSON before deploying:
- Online: https://jsonlint.com/
- VS Code: JSON validation is built-in (shows errors)
- Command line: `python -m json.tool 819605-myquiz.json`

## 📚 Need More Help?

See full documentation in `README.md` in the same directory.
