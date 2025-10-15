# Quiz System - Data Management Guide

## 📁 Directory Structure

```
teaching/
├── data/
│   └── quizzes/
│       ├── quiz-config.json          # Main configuration file
│       ├── 819605-demo.json          # Demo quiz for course 819605
│       ├── 819605-quiz1.json         # Quiz 1 for course 819605
│       ├── 819605-quiz2.json         # Quiz 2 for course 819605
│       └── [other-course]-quiz.json  # Add more quizzes here
└── 819605-2-2568-demo.html           # Quiz interface page
```

## 🚀 How to Add a New Quiz

### Step 1: Create Quiz JSON File

Create a new file in `data/quizzes/` directory with the naming pattern:
`[courseCode]-[quizName].json`

Example: `819605-midterm.json`

```json
{
  "id": "midterm",
  "courseCode": "819605",
  "title": "Midterm Exam - Discrete Mathematics",
  "duration": 90,
  "questions": [
    {
      "id": 1,
      "question": "Your question here?",
      "type": "multiple-choice",
      "points": 10,
      "options": [
        "Option A",
        "Option B",
        "Option C",
        "Option D"
      ],
      "correctAnswer": 0
    },
    {
      "id": 2,
      "question": "Essay question here?",
      "type": "text",
      "points": 20,
      "correctAnswer": "Sample correct answer for reference"
    }
  ]
}
```

### Step 2: Register Quiz in Configuration

Edit `data/quizzes/quiz-config.json` and add your quiz to the course:

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
        },
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

## 📝 Quiz JSON Format Reference

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier for the quiz |
| `courseCode` | string | Course code (e.g., "819605") |
| `title` | string | Quiz title shown to students |
| `duration` | number | Time limit in minutes |
| `questions` | array | Array of question objects |

### Question Object Format

#### Multiple Choice Questions

```json
{
  "id": 1,
  "question": "Question text here",
  "type": "multiple-choice",
  "points": 10,
  "options": [
    "Option 1",
    "Option 2",
    "Option 3",
    "Option 4"
  ],
  "correctAnswer": 0
}
```

- `correctAnswer`: Index of correct option (0-based)

#### Text Answer Questions

```json
{
  "id": 2,
  "question": "Essay or short answer question",
  "type": "text",
  "points": 20,
  "correctAnswer": "Reference answer for grading"
}
```

- `correctAnswer`: Text answer for instructor reference (manual grading required)

## 🎓 How to Add a New Course

### Step 1: Create Quiz Files

Create quiz files following the pattern: `[newCourseCode]-[quizName].json`

Example for course 720201:
- `720201-demo.json`
- `720201-quiz1.json`

### Step 2: Add Course to Configuration

Edit `data/quizzes/quiz-config.json`:

```json
{
  "courses": {
    "819605": {
      "courseName": "Discrete Mathematics",
      "courseNameThai": "วิยุตคณิต",
      "quizzes": [...]
    },
    "720201": {
      "courseName": "Programming Fundamentals",
      "courseNameThai": "การเขียนโปรแกรมเบื้องต้น",
      "quizzes": [
        {
          "id": "demo",
          "file": "720201-demo.json",
          "displayName": "Demo Quiz",
          "enabled": true
        }
      ]
    }
  }
}
```

### Step 3: Create Course Quiz Page

Copy `819605-2-2568-demo.html` and rename it (e.g., `720201-demo.html`)

Update the configuration section:

```javascript
const QUIZ_CONFIG = {
    courseCode: '720201', // Change to new course code
    quizDataPath: 'data/quizzes/',
    configFile: 'quiz-config.json'
};
```

## 🔧 Configuration Options

### Enable/Disable Quizzes

Set `enabled: false` in quiz-config.json to hide a quiz:

```json
{
  "id": "quiz1",
  "file": "819605-quiz1.json",
  "displayName": "Quiz 1",
  "enabled": false
}
```

### Adjust Quiz Duration

Edit the quiz JSON file:

```json
{
  "duration": 60
}
```

### Change Point Values

Edit individual questions in the quiz JSON:

```json
{
  "id": 1,
  "points": 15
}
```

## 📊 Data Format Examples

### Example: Complete Quiz File

```json
{
  "id": "final",
  "courseCode": "819605",
  "title": "Final Exam - Discrete Mathematics",
  "duration": 120,
  "questions": [
    {
      "id": 1,
      "question": "What is the cardinality of power set of {1,2,3}?",
      "type": "multiple-choice",
      "points": 5,
      "options": ["3", "6", "8", "9"],
      "correctAnswer": 2
    },
    {
      "id": 2,
      "question": "Prove by mathematical induction that 1+2+...+n = n(n+1)/2",
      "type": "text",
      "points": 25,
      "correctAnswer": "Base case: n=1, 1=1(1+1)/2=1. Inductive step: Assume true for k, prove for k+1..."
    }
  ]
}
```

## 🛠️ Troubleshooting

### Quiz Not Appearing in Dropdown

1. Check that `enabled: true` in quiz-config.json
2. Verify the quiz file exists in `data/quizzes/`
3. Check browser console for error messages
4. Ensure JSON syntax is valid (use JSON validator)

### Questions Not Loading

1. Verify quiz file path in quiz-config.json
2. Check that `id` in quiz file matches `id` in config
3. Ensure all required fields are present
4. Validate JSON syntax

### Browser Cache Issues

If changes don't appear:
1. Hard refresh: Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)
2. Clear browser cache
3. Open in incognito/private mode

## 📝 Best Practices

1. **Always test new quizzes** with demo data before using with students
2. **Backup quiz files** before making major changes
3. **Use descriptive IDs** (e.g., "midterm2024" instead of "test1")
4. **Keep question IDs sequential** within each quiz
5. **Validate JSON** before deploying (use jsonlint.com)
6. **Store sensitive data** (API keys) separately, not in quiz files

## 🔐 Security Notes

- Quiz answer keys are visible in JSON files
- Host quiz files on secure server
- Use backend API for production (see GOOGLE_SHEETS_SETUP_GUIDE.md)
- Consider encrypting answer keys for high-stakes exams

## 📞 Support

For questions or issues:
1. Check this README first
2. Review ANTI_CHEATING_SYSTEM_DOCS.md for anti-cheating features
3. See GOOGLE_SHEETS_SETUP_GUIDE.md for data storage setup
