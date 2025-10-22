/**
 * Quiz Result Submission Handler
 * Google Apps Script for 819605 - Discrete Mathematics
 * Southeast Asia University
 * 
 * This script receives quiz submissions from the web application,
 * validates answers, calculates scores, and stores results in Google Sheets.
 */

// ========== CONFIGURATION ==========
const CONFIG = {
  // Spreadsheet configuration
  SPREADSHEET_ID: 'YOUR_SPREADSHEET_ID_HERE', // Replace with your Google Sheets ID
  SHEETS: {
    QUIZ_DATA: 'QuizData',      // Sheet containing quiz questions and answers
    SUBMISSIONS: 'Submissions',  // Sheet to store student submissions
    LOG: 'Log'                   // Sheet for error/activity logs
  },
  
  // Course configuration
  COURSE_CODE: '819605',
  
  // Grading thresholds (must match client-side CONFIG.GRADING)
  GRADING: {
    A: 80,
    B: 70,
    C: 60,
    D: 50
  }
};

// ========== MAIN HANDLER ==========
/**
 * Handles POST requests from the quiz application
 * This is the entry point for all submissions
 */
function doPost(e) {
  try {
    // Parse incoming data
    const data = JSON.parse(e.postData.contents);
    
    // Log the submission attempt
    logActivity('Submission received', data.studentId);
    
    // Validate the submission
    const validation = validateSubmission(data);
    if (!validation.valid) {
      return createResponse(false, validation.error);
    }
    
    // Load quiz data from spreadsheet
    const quizData = loadQuizData(data.quizId);
    if (!quizData) {
      return createResponse(false, 'Quiz data not found');
    }
    
    // Grade the submission (server-side validation)
    const gradingResult = gradeSubmission(data, quizData);
    
    // Save to spreadsheet
    const saved = saveSubmission(data, gradingResult);
    if (!saved) {
      return createResponse(false, 'Failed to save submission');
    }
    
    // Return success response with server-computed results
    return createResponse(true, 'Submission successful', {
      computed: {
        correct: gradingResult.correctCount,
        incorrect: gradingResult.incorrectCount,
        score: gradingResult.score,
        totalPoints: gradingResult.totalPoints,
        percentage: gradingResult.percentage,
        grade: gradingResult.grade
      },
      submissionId: saved.submissionId,
      timestamp: new Date().toISOString()
    });
    
  } catch (error) {
    logError('doPost error', error);
    return createResponse(false, 'Server error: ' + error.message);
  }
}

// ========== VALIDATION ==========
/**
 * Validates the incoming submission data
 */
function validateSubmission(data) {
  // Check required fields
  if (!data.studentId || !data.studentName) {
    return { valid: false, error: 'Missing student information' };
  }
  
  if (!data.quizId) {
    return { valid: false, error: 'Missing quiz ID' };
  }
  
  if (!Array.isArray(data.answers) || data.answers.length === 0) {
    return { valid: false, error: 'Missing or invalid answers' };
  }
  
  // Validate student ID format (adjust pattern as needed)
  if (!/^\d{10}$/.test(data.studentId)) {
    return { valid: false, error: 'Invalid student ID format' };
  }
  
  return { valid: true };
}

// ========== QUIZ DATA LOADER ==========
/**
 * Loads quiz questions and correct answers from Google Sheets
 * Expected format in QuizData sheet:
 * | QuizID | QuestionID | Question | Type | Options (JSON) | CorrectAnswer | Points | Explanation |
 */
function loadQuizData(quizId) {
  try {
    const ss = SpreadsheetApp.openById(CONFIG.SPREADSHEET_ID);
    const sheet = ss.getSheetByName(CONFIG.SHEETS.QUIZ_DATA);
    
    if (!sheet) {
      throw new Error('QuizData sheet not found');
    }
    
    const data = sheet.getDataRange().getValues();
    const headers = data[0];
    
    // Find column indices
    const colIndices = {
      quizId: headers.indexOf('QuizID'),
      questionId: headers.indexOf('QuestionID'),
      question: headers.indexOf('Question'),
      type: headers.indexOf('Type'),
      options: headers.indexOf('Options'),
      correctAnswer: headers.indexOf('CorrectAnswer'),
      points: headers.indexOf('Points'),
      explanation: headers.indexOf('Explanation')
    };
    
    // Extract questions for this quiz
    const questions = [];
    for (let i = 1; i < data.length; i++) {
      const row = data[i];
      if (row[colIndices.quizId] === quizId) {
        questions.push({
          questionId: row[colIndices.questionId],
          question: row[colIndices.question],
          type: row[colIndices.type],
          options: row[colIndices.options] ? JSON.parse(row[colIndices.options]) : null,
          correctAnswer: row[colIndices.correctAnswer],
          points: parseFloat(row[colIndices.points]) || 0,
          explanation: row[colIndices.explanation] || ''
        });
      }
    }
    
    return {
      quizId: quizId,
      questions: questions
    };
    
  } catch (error) {
    logError('loadQuizData error', error);
    return null;
  }
}

// ========== GRADING ENGINE ==========
/**
 * Grades the student's submission against correct answers
 * This is the authoritative grading (server-side validation)
 */
function gradeSubmission(submission, quizData) {
  let correctCount = 0;
  let incorrectCount = 0;
  let score = 0;
  let totalPoints = 0;
  
  const gradedAnswers = [];
  
  // Create a map of questions for quick lookup
  const questionMap = {};
  quizData.questions.forEach(q => {
    questionMap[q.questionId] = q;
  });
  
  // Grade each answer
  submission.answers.forEach(answer => {
    const question = questionMap[answer.questionId];
    
    if (!question) {
      // Question not found - skip
      gradedAnswers.push({
        questionId: answer.questionId,
        userAnswer: answer.userAnswer,
        isCorrect: false,
        points: 0,
        error: 'Question not found'
      });
      return;
    }
    
    totalPoints += question.points;
    
    // Grade based on question type
    let isCorrect = false;
    if (question.type === 'multiple-choice') {
      // For multiple choice, compare index
      isCorrect = parseInt(answer.userAnswer) === parseInt(question.correctAnswer);
    } else if (question.type === 'text') {
      // For text answers, could implement fuzzy matching or exact match
      // Currently treating as manual grading (always false)
      isCorrect = false;
    }
    
    if (isCorrect) {
      correctCount++;
      score += question.points;
    } else {
      incorrectCount++;
    }
    
    gradedAnswers.push({
      questionId: answer.questionId,
      userAnswer: answer.userAnswer,
      correctAnswer: question.correctAnswer,
      isCorrect: isCorrect,
      pointsEarned: isCorrect ? question.points : 0,
      pointsPossible: question.points
    });
  });
  
  // Calculate percentage and grade
  const percentage = totalPoints > 0 ? Math.round((score / totalPoints) * 100) : 0;
  const grade = calculateGrade(percentage);
  
  return {
    correctCount: correctCount,
    incorrectCount: incorrectCount,
    score: score,
    totalPoints: totalPoints,
    percentage: percentage,
    grade: grade,
    gradedAnswers: gradedAnswers
  };
}

/**
 * Calculates letter grade based on percentage
 */
function calculateGrade(percentage) {
  if (percentage >= CONFIG.GRADING.A) return 'A';
  if (percentage >= CONFIG.GRADING.B) return 'B';
  if (percentage >= CONFIG.GRADING.C) return 'C';
  if (percentage >= CONFIG.GRADING.D) return 'D';
  return 'F';
}

// ========== DATA PERSISTENCE ==========
/**
 * Saves the submission to Google Sheets
 * Expected format in Submissions sheet:
 * | SubmissionID | Timestamp | StudentID | StudentName | QuizID | QuizTitle | 
 * | Score | TotalPoints | Percentage | Grade | TimeUsed | TabSwitches | UserAgent | Answers (JSON) |
 */
function saveSubmission(submission, gradingResult) {
  try {
    const ss = SpreadsheetApp.openById(CONFIG.SPREADSHEET_ID);
    let sheet = ss.getSheetByName(CONFIG.SHEETS.SUBMISSIONS);
    
    // Create sheet if it doesn't exist
    if (!sheet) {
      sheet = ss.insertSheet(CONFIG.SHEETS.SUBMISSIONS);
      // Add headers
      sheet.appendRow([
        'SubmissionID', 'Timestamp', 'StudentID', 'StudentName', 'QuizID', 'QuizTitle',
        'Score', 'TotalPoints', 'Percentage', 'Grade', 'TimeUsedSec', 
        'TabSwitchCount', 'UserAgent', 'ClientScore', 'ClientGrade', 'Answers (JSON)'
      ]);
    }
    
    // Generate unique submission ID
    const submissionId = Utilities.getUuid();
    const timestamp = new Date().toISOString();
    
    // Prepare row data
    const rowData = [
      submissionId,
      timestamp,
      submission.studentId,
      submission.studentName,
      submission.quizId,
      submission.quizTitle || '',
      gradingResult.score,
      gradingResult.totalPoints,
      gradingResult.percentage,
      gradingResult.grade,
      submission.timeUsedSec || 0,
      submission.clientMeta?.tabSwitchCount || 0,
      submission.clientMeta?.userAgent || '',
      submission.clientMeta?.clientReported?.score || '',
      submission.clientMeta?.clientReported?.grade || '',
      JSON.stringify(gradingResult.gradedAnswers)
    ];
    
    // Append to sheet
    sheet.appendRow(rowData);
    
    return {
      success: true,
      submissionId: submissionId
    };
    
  } catch (error) {
    logError('saveSubmission error', error);
    return null;
  }
}

// ========== LOGGING ==========
/**
 * Logs activity to the Log sheet
 */
function logActivity(message, details) {
  try {
    const ss = SpreadsheetApp.openById(CONFIG.SPREADSHEET_ID);
    let sheet = ss.getSheetByName(CONFIG.SHEETS.LOG);
    
    if (!sheet) {
      sheet = ss.insertSheet(CONFIG.SHEETS.LOG);
      sheet.appendRow(['Timestamp', 'Type', 'Message', 'Details']);
    }
    
    sheet.appendRow([
      new Date().toISOString(),
      'INFO',
      message,
      JSON.stringify(details)
    ]);
  } catch (error) {
    // Silent fail for logging
    console.error('Logging error:', error);
  }
}

/**
 * Logs errors to the Log sheet
 */
function logError(message, error) {
  try {
    const ss = SpreadsheetApp.openById(CONFIG.SPREADSHEET_ID);
    let sheet = ss.getSheetByName(CONFIG.SHEETS.LOG);
    
    if (!sheet) {
      sheet = ss.insertSheet(CONFIG.SHEETS.LOG);
      sheet.appendRow(['Timestamp', 'Type', 'Message', 'Details']);
    }
    
    sheet.appendRow([
      new Date().toISOString(),
      'ERROR',
      message,
      error.toString() + '\n' + error.stack
    ]);
  } catch (e) {
    console.error('Error logging error:', e);
  }
}

// ========== RESPONSE HELPER ==========
/**
 * Creates a standardized JSON response
 */
function createResponse(success, message, data = {}) {
  const response = {
    ok: success,
    message: message,
    ...data
  };
  
  return ContentService
    .createTextOutput(JSON.stringify(response))
    .setMimeType(ContentService.MimeType.JSON);
}

// ========== UTILITY FUNCTIONS ==========
/**
 * Test function to verify the script setup
 * Run this from the Apps Script editor to test
 */
function testSetup() {
  Logger.log('Testing quiz submission system...');
  
  // Test spreadsheet access
  try {
    const ss = SpreadsheetApp.openById(CONFIG.SPREADSHEET_ID);
    Logger.log('✓ Spreadsheet access OK');
    Logger.log('Spreadsheet name: ' + ss.getName());
  } catch (error) {
    Logger.log('✗ Spreadsheet access FAILED: ' + error.message);
    return;
  }
  
  // Test quiz data loading
  try {
    const quizData = loadQuizData('demo');
    if (quizData && quizData.questions.length > 0) {
      Logger.log('✓ Quiz data loading OK');
      Logger.log('Found ' + quizData.questions.length + ' questions for demo quiz');
    } else {
      Logger.log('⚠ Quiz data loading returned empty result');
    }
  } catch (error) {
    Logger.log('✗ Quiz data loading FAILED: ' + error.message);
  }
  
  Logger.log('Test complete!');
}

/**
 * Creates sample quiz data in the QuizData sheet
 * Run this once to set up sample data
 */
function createSampleQuizData() {
  const ss = SpreadsheetApp.openById(CONFIG.SPREADSHEET_ID);
  let sheet = ss.getSheetByName(CONFIG.SHEETS.QUIZ_DATA);
  
  if (!sheet) {
    sheet = ss.insertSheet(CONFIG.SHEETS.QUIZ_DATA);
  }
  
  // Clear existing data
  sheet.clear();
  
  // Add headers
  sheet.appendRow(['QuizID', 'QuestionID', 'Question', 'Type', 'Options', 'CorrectAnswer', 'Points', 'Explanation']);
  
  // Add sample questions for demo quiz
  const sampleQuestions = [
    ['demo', 'q1', 'What is 2 + 2?', 'multiple-choice', '["2", "3", "4", "5"]', 2, 10, 'Basic arithmetic'],
    ['demo', 'q2', 'What is the capital of Thailand?', 'multiple-choice', '["Bangkok", "Chiang Mai", "Phuket", "Pattaya"]', 0, 10, 'Geography question'],
    ['demo', 'q3', 'Is the sky blue?', 'multiple-choice', '["True", "False"]', 0, 10, 'Simple true/false']
  ];
  
  sampleQuestions.forEach(q => sheet.appendRow(q));
  
  Logger.log('Sample quiz data created!');
}
