# Migration Guide - Converting Existing Quizzes

## 📋 Overview

This guide helps you convert quizzes from the old embedded format to the new external JSON format.

## 🔄 Migration Process

### Step 1: Identify Your Current Quiz Data

In your old HTML file, find the quiz data:

```javascript
const quizData = {
    demo: {
        title: "Demo Quiz",
        duration: 30,
        questions: [...]
    }
};
```

### Step 2: Extract Each Quiz

For each quiz in `quizData`, create a separate JSON file.

**Example: Converting "demo" quiz**

Old format (in HTML):
```javascript
demo: {
    title: "Demo Quiz (ทดสอบระบบ)",
    duration: 30,
    questions: [
        {
            id: 1,
            type: "multiple-choice",
            question: "What is a set?",
            points: 10,
            options: ["A", "B", "C", "D"],
            correctAnswer: 1
        }
    ]
}
```

New format (in `819605-demo.json`):
```json
{
  "id": "demo",
  "courseCode": "819605",
  "title": "Demo Quiz (ทดสอบระบบ)",
  "duration": 30,
  "questions": [
    {
      "id": 1,
      "type": "multiple-choice",
      "question": "What is a set?",
      "points": 10,
      "options": ["A", "B", "C", "D"],
      "correctAnswer": 1
    }
  ]
}
```

### Step 3: Add Required Fields

The JSON format requires two additional top-level fields:

```json
{
  "id": "demo",           ← Add this (quiz identifier)
  "courseCode": "819605", ← Add this (course code)
  "title": "...",
  "duration": 30,
  "questions": [...]
}
```

### Step 4: Register in Configuration

Add your quiz to `quiz-config.json`:

```json
{
  "courses": {
    "819605": {
      "courseName": "Discrete Mathematics",
      "courseNameThai": "วิยุตคณิต",
      "quizzes": [
        {
          "id": "demo",
          "file": "819605-demo.json",
          "displayName": "Demo Quiz (ทดสอบระบบ)",
          "enabled": true
        }
      ]
    }
  }
}
```

## 🛠️ Automated Conversion Script

Use this Python script to help with conversion:

```python
import json

# Your old quizData object (as Python dict)
old_quiz_data = {
    "demo": {
        "title": "Demo Quiz",
        "duration": 30,
        "questions": [...]
    },
    "quiz1": {
        "title": "Quiz 1",
        "duration": 45,
        "questions": [...]
    }
}

# Course code
course_code = "819605"

# Convert each quiz
for quiz_id, quiz_content in old_quiz_data.items():
    # Add required fields
    new_quiz = {
        "id": quiz_id,
        "courseCode": course_code,
        **quiz_content
    }
    
    # Save to file
    filename = f"{course_code}-{quiz_id}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(new_quiz, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Created: {filename}")
```

## 📝 Detailed Conversion Steps

### Converting Multiple Choice Questions

No changes needed! Just copy as-is:

```json
{
  "id": 1,
  "type": "multiple-choice",
  "question": "Your question?",
  "points": 10,
  "options": ["A", "B", "C", "D"],
  "correctAnswer": 0
}
```

### Converting Text Questions

No changes needed! Just copy as-is:

```json
{
  "id": 2,
  "type": "text",
  "question": "Explain...",
  "points": 20,
  "correctAnswer": "Sample answer"
}
```

### Converting Questions with HTML

Questions can contain HTML - no changes needed:

```json
{
  "question": "What is <strong>2 + 2</strong>?",
  "type": "multiple-choice",
  "options": ["3", "4", "5", "6"],
  "correctAnswer": 1
}
```

### Converting Questions with Math Notation

If you use math notation, it works the same:

```json
{
  "question": "Solve: ∑(i=1 to n) i = ?",
  "type": "multiple-choice",
  "options": ["n", "n²", "n(n+1)/2", "2n"],
  "correctAnswer": 2
}
```

## ⚠️ Common Pitfalls

### 1. JavaScript vs JSON Syntax

**JavaScript (old):**
```javascript
{
    id: 1,                    // No quotes on keys
    question: "Test",         // Single quotes
    correctAnswer: 1,         // Trailing comma OK
}
```

**JSON (new):**
```json
{
  "id": 1,                    
  "question": "Test",         
  "correctAnswer": 1          
}
```

Key differences:
- ✅ Use double quotes for keys and strings
- ✅ Remove trailing commas
- ✅ No comments allowed in JSON

### 2. File Naming Convention

Use this pattern: `{courseCode}-{quizId}.json`

✅ Good:
- `819605-demo.json`
- `819605-midterm.json`
- `720201-quiz1.json`

❌ Bad:
- `demo.json` (missing course code)
- `819605_demo.json` (use hyphen, not underscore)
- `Quiz1.json` (inconsistent case)

### 3. Quiz ID Consistency

The quiz ID must match in 3 places:

1. Filename: `819605-**demo**.json`
2. Quiz file: `"id": "**demo**"`
3. Config file: `"id": "**demo**"`

### 4. Question IDs

Keep question IDs sequential:

✅ Good:
```json
{"id": 1}, {"id": 2}, {"id": 3}
```

❌ Bad:
```json
{"id": 1}, {"id": 3}, {"id": 2}  // Out of order
{"id": 1}, {"id": 1}, {"id": 2}  // Duplicate
```

## 🧪 Testing Your Migration

After converting, test each quiz:

### 1. Validate JSON
```bash
python validate_quiz.py 819605-demo.json
```

### 2. Load in Browser
1. Open quiz page
2. Select your quiz from dropdown
3. Check that all questions load
4. Verify options display correctly

### 3. Test Functionality
- [ ] Questions navigate correctly
- [ ] Timer works
- [ ] Answers can be selected
- [ ] Submit button works
- [ ] Results display correctly

## 📊 Example: Complete Migration

### Before (in HTML file)

```javascript
const quizData = {
    midterm: {
        title: "Midterm Exam",
        duration: 90,
        questions: [
            {
                id: 1,
                type: "multiple-choice",
                question: "What is 2+2?",
                points: 5,
                options: ["3", "4", "5", "6"],
                correctAnswer: 1
            },
            {
                id: 2,
                type: "text",
                question: "Explain sets.",
                points: 15,
                correctAnswer: "A set is a collection..."
            }
        ]
    }
};
```

### After Migration

**File: 819605-midterm.json**
```json
{
  "id": "midterm",
  "courseCode": "819605",
  "title": "Midterm Exam",
  "duration": 90,
  "questions": [
    {
      "id": 1,
      "type": "multiple-choice",
      "question": "What is 2+2?",
      "points": 5,
      "options": ["3", "4", "5", "6"],
      "correctAnswer": 1
    },
    {
      "id": 2,
      "type": "text",
      "question": "Explain sets.",
      "points": 15,
      "correctAnswer": "A set is a collection..."
    }
  ]
}
```

**In quiz-config.json:**
```json
{
  "courses": {
    "819605": {
      "quizzes": [
        {
          "id": "midterm",
          "file": "819605-midterm.json",
          "displayName": "Midterm Exam",
          "enabled": true
        }
      ]
    }
  }
}
```

## 🔧 Troubleshooting

### Quiz doesn't appear in dropdown

**Possible causes:**
1. Not registered in `quiz-config.json`
2. `enabled: false` in config
3. File name doesn't match config
4. JSON syntax error

**Solution:**
```bash
# Validate the files
python validate_quiz.py quiz-config.json
python validate_quiz.py 819605-yourquiz.json

# Check browser console for errors
```

### Questions not loading

**Possible causes:**
1. Wrong file path in config
2. Quiz ID mismatch
3. Invalid JSON format

**Solution:**
```bash
# Validate JSON syntax
python -m json.tool 819605-yourquiz.json

# Check browser console (F12) for error messages
```

### Answers not saving

**Possible causes:**
1. `correctAnswer` field missing
2. `correctAnswer` value out of range
3. Wrong data type (string instead of number)

**Solution:**
```bash
# Run validator to find issues
python validate_quiz.py 819605-yourquiz.json
```

## 📚 Best Practices

1. **Migrate one quiz at a time** - Test each before moving to next
2. **Keep backups** - Save old HTML file before changes
3. **Use validator** - Run `validate_quiz.py` after each conversion
4. **Test thoroughly** - Complete full quiz in browser after migration
5. **Version control** - Commit working versions to Git

## 🎯 Quick Checklist

Use this checklist for each quiz migration:

- [ ] Extract quiz data from HTML
- [ ] Create new JSON file with correct naming
- [ ] Add `id` and `courseCode` fields
- [ ] Convert JavaScript syntax to JSON
- [ ] Remove trailing commas
- [ ] Add quiz to `quiz-config.json`
- [ ] Validate with `validate_quiz.py`
- [ ] Test in browser
- [ ] Verify all questions load
- [ ] Test quiz submission
- [ ] Commit to version control

## 💡 Tips

- Use a JSON formatter/validator while editing
- VS Code has built-in JSON validation
- Test in incognito mode to avoid cache issues
- Keep question IDs sequential
- Document any special formatting in question text

---

**Need help?** See `README.md` for full documentation or `QUICK_START.md` for basic usage.
