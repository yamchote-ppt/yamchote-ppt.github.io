/**
 * Quiz System - Modular JavaScript
 * 819605 - Discrete Mathematics
 * Southeast Asia University
 */

// ========== STATE MANAGEMENT ==========
const QuizState = {
    quizConfig: null,
    quizData: {},
    currentQuiz: null,
    currentQuestionIndex: 0,
    userAnswers: [],
    timerInterval: null,
    timeRemaining: 0,
    quizStartTime: null,
    studentInfo: {},
    tabSwitchCount: 0,
    hasLeftPage: false,
    devToolsInterval: null
};

// ========== QUIZ DATA LOADER ==========
class QuizDataLoader {
    static async loadQuizConfig() {
        try {
            const res = await fetch(CONFIG.QUIZ.quizDataPath + CONFIG.QUIZ.configFile);
            if (!res.ok) throw new Error(`Failed to load quiz config: ${res.status}`);
            const conf = await res.json();
            return conf.courses[CONFIG.QUIZ.courseCode];
        } catch (error) {
            console.error('Error loading quiz config:', error);
            throw error;
        }
    }

    static async loadQuizData(quizInfo) {
        try {
            const res = await fetch(CONFIG.QUIZ.quizDataPath + quizInfo.file);
            if (!res.ok) throw new Error(`Failed to load quiz data: ${res.status}`);
            return await res.json();
        } catch (error) {
            console.error('Error loading quiz data:', error);
            throw error;
        }
    }
}

// ========== QUIZ UI MANAGER ==========
class QuizUI {
    static initializeQuizSelection(quizConfig) {
        const quizSelect = document.getElementById('quizSelect');
        quizSelect.innerHTML = '<option value="">-- กรุณาเลือกข้อสอบ --</option>';

        for (const quiz of quizConfig.quizzes) {
            if (!quiz.enabled) continue;
            const option = document.createElement('option');
            option.value = quiz.id;
            option.textContent = quiz.displayName;
            quizSelect.appendChild(option);
        }
    }

    static updateQuizInfo(quiz) {
        document.getElementById('totalQuestions').textContent = quiz.questions.length;
        document.getElementById('quizDuration').textContent = quiz.duration;
        document.getElementById('totalPoints').textContent = 
            quiz.questions.reduce((sum, q) => sum + q.points, 0);
    }

    static showScreen(screenId) {
        const screens = ['quizStart', 'loading', 'quizContainer', 'quizResults'];
        screens.forEach(id => {
            const element = document.getElementById(id);
            if (element) {
                if (id === screenId) {
                    if (id === 'quizContainer' || id === 'quizResults') {
                        element.classList.add('active');
                    } else {
                        element.style.display = 'block';
                    }
                } else {
                    if (id === 'quizContainer' || id === 'quizResults') {
                        element.classList.remove('active');
                    } else {
                        element.style.display = 'none';
                    }
                }
            }
        });
    }

    static displayQuestion(quiz, questionIndex, userAnswers) {
        const question = quiz.questions[questionIndex];
        
        // Update header info
        document.getElementById('currentQuestion').textContent = questionIndex + 1;
        document.getElementById('totalQuestionsDisplay').textContent = quiz.questions.length;
        document.getElementById('questionNumber').textContent = `Question ${questionIndex + 1}`;
        document.getElementById('questionType').textContent = 
            question.type === 'multiple-choice' ? 'Multiple Choice' : 'Text Answer';
        document.getElementById('questionPoints').textContent = `${question.points} คะแนน`;
        document.getElementById('questionText').innerHTML = question.question;

        // Render answer options
        const optionsContainer = document.getElementById('answerOptions');
        optionsContainer.innerHTML = '';

        if (question.type === 'multiple-choice') {
            this.renderMultipleChoice(question, questionIndex, userAnswers, optionsContainer);
        } else {
            this.renderTextAnswer(questionIndex, userAnswers, optionsContainer);
        }

        // Update navigation buttons
        document.getElementById('prevBtn').disabled = questionIndex === 0;
        const nextBtn = document.getElementById('nextBtn');
        nextBtn.style.display = questionIndex === quiz.questions.length - 1 ? 'none' : 'inline-block';
    }

    static renderMultipleChoice(question, questionIndex, userAnswers, container) {
        question.options.forEach((option, idx) => {
            const div = document.createElement('div');
            div.className = 'answer-option' + (userAnswers[questionIndex] === idx ? ' selected' : '');
            div.innerHTML = `
                <input type="radio" name="answer" id="option${idx}" value="${idx}" 
                    ${userAnswers[questionIndex] === idx ? 'checked' : ''}>
                <label for="option${idx}">${String.fromCharCode(65 + idx)}. ${option}</label>
            `;
            div.addEventListener('click', () => QuizController.selectAnswer(idx));
            container.appendChild(div);
        });
    }

    static renderTextAnswer(questionIndex, userAnswers, container) {
        const textarea = document.createElement('textarea');
        textarea.className = 'text-answer';
        textarea.placeholder = 'พิมพ์คำตอบของคุณที่นี่...';
        textarea.value = userAnswers[questionIndex] || '';
        textarea.addEventListener('input', function() {
            QuizState.userAnswers[QuizState.currentQuestionIndex] = this.value;
            QuizNavigator.updateNavigator();
        });
        container.appendChild(textarea);
    }

    static displayResults(quiz, studentInfo, results) {
        document.getElementById('resultQuizName').textContent = quiz.title;
        document.getElementById('resultStudentName').textContent = studentInfo.studentName;
        document.getElementById('resultStudentId').textContent = studentInfo.studentId;
        document.getElementById('correctAnswers').textContent = results.correctCount;
        document.getElementById('incorrectAnswers').textContent = results.incorrectCount;
        document.getElementById('scoreObtained').textContent = results.earned;
        document.getElementById('scorePossible').textContent = results.totalPoints;
        document.getElementById('scorePercentage').textContent = results.percentage + '%';
        document.getElementById('timeUsed').textContent = results.timeUsed;

        const gradeBadge = document.getElementById('gradeBadge');
        gradeBadge.textContent = results.grade;
        gradeBadge.className = 'grade-badge grade-' + results.grade.toLowerCase();
    }
}

// ========== QUIZ NAVIGATOR ==========
class QuizNavigator {
    static create() {
        const grid = document.getElementById('questionGrid');
        grid.innerHTML = '';
        
        QuizState.currentQuiz.questions.forEach((_, index) => {
            const button = document.createElement('button');
            button.type = 'button';
            button.className = 'question-nav-btn';
            button.textContent = index + 1;
            button.onclick = () => {
                QuizState.currentQuestionIndex = index;
                QuizUI.displayQuestion(
                    QuizState.currentQuiz,
                    QuizState.currentQuestionIndex,
                    QuizState.userAnswers
                );
                this.updateNavigator();
            };
            grid.appendChild(button);
        });
        
        this.updateNavigator();
    }

    static updateNavigator() {
        document.querySelectorAll('.question-nav-btn').forEach((btn, index) => {
            btn.classList.remove('current', 'answered');
            if (index === QuizState.currentQuestionIndex) {
                btn.classList.add('current');
            } else if (QuizState.userAnswers[index] !== null && QuizState.userAnswers[index] !== '') {
                btn.classList.add('answered');
            }
        });
    }
}

// ========== QUIZ TIMER ==========
class QuizTimer {
    static start(duration) {
        QuizState.timeRemaining = duration * 60;
        this.updateDisplay();
        
        QuizState.timerInterval = setInterval(() => {
            QuizState.timeRemaining--;
            this.updateDisplay();
            
            if (QuizState.timeRemaining <= CONFIG.TIMER.warningThreshold) {
                document.getElementById('timer').classList.add('warning');
            }
            
            if (QuizState.timeRemaining <= 0) {
                clearInterval(QuizState.timerInterval);
                alert('หมดเวลา! ระบบจะส่งข้อสอบอัตโนมัติ');
                QuizController.submitQuiz();
            }
        }, CONFIG.TIMER.updateInterval);
    }

    static updateDisplay() {
        const minutes = Math.floor(QuizState.timeRemaining / 60);
        const seconds = QuizState.timeRemaining % 60;
        document.getElementById('timeRemaining').textContent = 
            `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }

    static stop() {
        if (QuizState.timerInterval) {
            clearInterval(QuizState.timerInterval);
            QuizState.timerInterval = null;
        }
    }
}

// ========== GRADING SYSTEM ==========
class GradingSystem {
    static calculateResults(quiz, userAnswers) {
        let correctCount = 0;
        let totalPoints = 0;
        let earned = 0;

        quiz.questions.forEach((question, index) => {
            totalPoints += question.points;
            if (question.type === 'multiple-choice' && userAnswers[index] === question.correctAnswer) {
                correctCount++;
                earned += question.points;
            }
        });

        const percentage = Math.round((earned / totalPoints) * 100);
        const grade = this.getGrade(percentage);

        return {
            correctCount,
            incorrectCount: quiz.questions.length - correctCount,
            totalPoints,
            earned,
            percentage,
            grade
        };
    }

    static getGrade(percentage) {
        if (percentage >= CONFIG.GRADING.A) return 'A';
        if (percentage >= CONFIG.GRADING.B) return 'B';
        if (percentage >= CONFIG.GRADING.C) return 'C';
        if (percentage >= CONFIG.GRADING.D) return 'D';
        return 'F';
    }
}

// ========== ANSWER REVIEW ==========
class AnswerReview {
    static display(quiz, userAnswers) {
        const reviewContainer = document.getElementById('answerReview');
        reviewContainer.innerHTML = '<h3 style="color:#002147; margin-bottom:1rem;">📋 รายละเอียดคำตอบ</h3>';

        quiz.questions.forEach((question, index) => {
            const userAnswer = userAnswers[index];
            const isCorrect = (question.type === 'multiple-choice') && (userAnswer === question.correctAnswer);
            
            const reviewDiv = document.createElement('div');
            reviewDiv.className = `review-question ${isCorrect ? 'correct' : 'incorrect'}`;
            
            const answerText = question.type === 'multiple-choice'
                ? (userAnswer != null ? question.options[userAnswer] : 'ไม่ได้ตอบ')
                : (userAnswer || 'ไม่ได้ตอบ');

            reviewDiv.innerHTML = `
                <div class="review-header">
                    <strong>ข้อที่ ${index + 1}</strong>
                    <span class="review-status ${isCorrect ? 'status-correct' : 'status-incorrect'}">
                        ${isCorrect ? '✓ ถูกต้อง' : '✗ ผิด'}
                    </span>
                </div>
                <p><strong>คำถาม:</strong> ${question.question}</p>
                <p><strong>คำตอบของคุณ:</strong> ${answerText}</p>
                ${question.type === 'multiple-choice' 
                    ? `<p><strong>เฉลย:</strong> ${question.options[question.correctAnswer]}</p>` 
                    : ''}
                ${question.explanation 
                    ? `<p style="color:#495057"><strong>คำอธิบาย:</strong> ${question.explanation}</p>` 
                    : ''}
            `;
            
            reviewContainer.appendChild(reviewDiv);
        });
    }
}

// ========== RESULTS SAVER ==========
class ResultsSaver {
    static async save(results) {
        // Save to localStorage as backup
        this.saveToLocalStorage(results);

        try {
            const payload = this.preparePayload(results);
            const response = await fetch(CONFIG.APP_SCRIPT_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });

            const data = await response.json();
            
            if (!data.ok) {
                console.warn('Server rejected submission:', data);
                this.showWarning('ไม่สามารถส่งข้อมูลไปยังเซิร์ฟเวอร์ กรุณาแจ้งอาจารย์ผู้สอน');
                return;
            }

            // Update UI with server-validated results
            this.updateUIWithServerResults(data.computed);
            this.showSuccessMessage();

        } catch (error) {
            console.error('Submit error:', error);
            this.showWarning('ไม่สามารถติดต่อเซิร์ฟเวอร์ได้ แต่ข้อมูลถูกบันทึกในเครื่องของคุณแล้ว');
        }
    }

    static saveToLocalStorage(results) {
        try {
            const allResults = JSON.parse(localStorage.getItem('quizResults') || '[]');
            allResults.push(results);
            localStorage.setItem('quizResults', JSON.stringify(allResults));
        } catch (error) {
            console.warn('LocalStorage backup failed', error);
        }
    }

    static preparePayload(results) {
        const answers = QuizState.currentQuiz.questions.map((question, idx) => {
            const questionId = question.id != null ? String(question.id) : `q${idx + 1}`;
            const userAnswer = QuizState.userAnswers[idx];
            
            return {
                questionId,
                userAnswer: question.type === 'multiple-choice' 
                    ? (userAnswer === null || userAnswer === '' ? null : Number(userAnswer))
                    : null
            };
        });

        return {
            studentId: QuizState.studentInfo.studentId,
            studentName: QuizState.studentInfo.studentName,
            quizId: QuizState.studentInfo.quizId,
            quizTitle: QuizState.currentQuiz.title,
            timeUsedSec: (new Date() - QuizState.quizStartTime) / 1000,
            answers,
            clientMeta: {
                clientReported: {
                    score: results.score,
                    totalPoints: results.totalPoints,
                    percentage: results.percentage,
                    grade: results.grade
                },
                tabSwitchCount: QuizState.tabSwitchCount,
                userAgent: navigator.userAgent
            }
        };
    }

    static updateUIWithServerResults(computed) {
        document.getElementById('correctAnswers').textContent = computed.correct;
        document.getElementById('incorrectAnswers').textContent = computed.incorrect;
        document.getElementById('scoreObtained').textContent = computed.score;
        document.getElementById('scorePossible').textContent = computed.totalPoints;
        document.getElementById('scorePercentage').textContent = computed.percentage + '%';
        
        const gradeBadge = document.getElementById('gradeBadge');
        gradeBadge.textContent = computed.grade;
        gradeBadge.className = 'grade-badge grade-' + computed.grade.toLowerCase();
    }

    static showSuccessMessage() {
        const successDiv = document.createElement('div');
        successDiv.className = 'alert alert-info';
        successDiv.innerHTML = `
            <span style="font-size:1.5rem;">✅</span>
            <div><strong>บันทึกสำเร็จ!</strong> ผลของคุณถูกส่งและตรวจคะแนนแล้ว</div>
        `;
        document.getElementById('quizResults').prepend(successDiv);
    }

    static showWarning(message) {
        const warningDiv = document.createElement('div');
        warningDiv.className = 'alert alert-info';
        warningDiv.style.backgroundColor = '#fff3cd';
        warningDiv.style.borderColor = '#ffc107';
        warningDiv.innerHTML = `
            <span style="font-size:1.5rem;">⚠️</span>
            <div>${message}</div>
        `;
        document.getElementById('quizResults').prepend(warningDiv);
    }
}

// ========== ANTI-CHEAT SYSTEM ==========
class AntiCheatSystem {
    static initialize() {
        QuizState.tabSwitchCount = 0;
        QuizState.hasLeftPage = false;

        // Visibility change detection
        document.addEventListener('visibilitychange', () => this.handleVisibilityChange());
        
        // Window blur detection
        window.addEventListener('blur', () => this.handleWindowBlur());
        
        // Developer tools detection
        QuizState.devToolsInterval = setInterval(() => this.detectDevTools(), CONFIG.ANTI_CHEAT.checkInterval);
        
        // Prevent copy/paste/cut
        document.addEventListener('copy', (e) => this.preventCopyPaste(e, 'คัดลอก'));
        document.addEventListener('paste', (e) => this.preventCopyPaste(e, 'วาง'));
        document.addEventListener('cut', (e) => this.preventCopyPaste(e, 'ตัด'));
        
        // Prevent right-click
        document.addEventListener('contextmenu', (e) => this.preventContextMenu(e));
        
        // Prevent page unload
        window.addEventListener('beforeunload', (e) => this.handleBeforeUnload(e));
    }

    static handleVisibilityChange() {
        if (!document.getElementById('quizContainer').classList.contains('active')) return;
        
        if (document.hidden) {
            QuizState.tabSwitchCount++;
            QuizState.hasLeftPage = true;
            
            if (QuizState.tabSwitchCount >= CONFIG.ANTI_CHEAT.maxTabSwitches) {
                alert('⚠️ เปลี่ยนแท็บบ่อย ระบบจะส่งข้อสอบอัตโนมัติ');
                this.autoSubmit('Tab switching detected');
            } else {
                alert(`⚠️ คำเตือน! (${QuizState.tabSwitchCount}/${CONFIG.ANTI_CHEAT.maxTabSwitches}) กรุณาอยู่ในหน้านี้ขณะทำข้อสอบ`);
            }
        }
    }

    static handleWindowBlur() {
        if (!document.getElementById('quizContainer').classList.contains('active')) return;
        
        QuizState.tabSwitchCount++;
        QuizState.hasLeftPage = true;
        
        if (QuizState.tabSwitchCount >= CONFIG.ANTI_CHEAT.maxTabSwitches) {
            alert('⚠️ คุณสลับโปรแกรม/หน้าต่างบ่อย ระบบจะส่งข้อสอบอัตโนมัติ');
            this.autoSubmit('Window focus lost');
        } else {
            alert(`⚠️ คำเตือน! (${QuizState.tabSwitchCount}/${CONFIG.ANTI_CHEAT.maxTabSwitches})`);
        }
    }

    static detectDevTools() {
        const threshold = CONFIG.ANTI_CHEAT.devToolsThreshold;
        const widthDiff = window.outerWidth - window.innerWidth;
        const heightDiff = window.outerHeight - window.innerHeight;
        
        if (widthDiff > threshold || heightDiff > threshold) {
            if (document.getElementById('quizContainer').classList.contains('active')) {
                alert('⚠️ ตรวจพบ Developer Tools ระบบจะส่งข้อสอบอัตโนมัติ');
                this.autoSubmit('Developer tools detected');
            }
        }
    }

    static preventCopyPaste(event, action) {
        if (document.getElementById('quizContainer').classList.contains('active')) {
            event.preventDefault();
            alert(`⚠️ ห้าม${action}ข้อความระหว่างทำข้อสอบ`);
        }
    }

    static preventContextMenu(event) {
        if (document.getElementById('quizContainer').classList.contains('active')) {
            event.preventDefault();
        }
    }

    static handleBeforeUnload(event) {
        if (document.getElementById('quizContainer').classList.contains('active')) {
            event.preventDefault();
            event.returnValue = '';
        }
    }

    static autoSubmit(reason) {
        QuizTimer.stop();
        
        if (QuizState.devToolsInterval) {
            clearInterval(QuizState.devToolsInterval);
            QuizState.devToolsInterval = null;
        }

        try {
            QuizController.closeSubmitModal();
        } catch (error) {
            // Ignore errors
        }

        QuizController.submitQuiz();

        setTimeout(() => {
            const warningDiv = document.createElement('div');
            warningDiv.className = 'alert alert-warning';
            warningDiv.innerHTML = `
                <span style="font-size:1.5rem;">⚠️</span>
                <div><strong>ข้อสอบถูกส่งอัตโนมัติ</strong><br>เหตุผล: ${reason}</div>
            `;
            document.getElementById('quizResults').prepend(warningDiv);
        }, 100);
    }

    static cleanup() {
        if (QuizState.devToolsInterval) {
            clearInterval(QuizState.devToolsInterval);
            QuizState.devToolsInterval = null;
        }
    }
}

// ========== QUIZ CONTROLLER ==========
class QuizController {
    static async initialize() {
        try {
            QuizState.quizConfig = await QuizDataLoader.loadQuizConfig();
            QuizUI.initializeQuizSelection(QuizState.quizConfig);
            this.attachEventListeners();
        } catch (error) {
            console.error('Initialization error:', error);
            alert('ไม่สามารถโหลดข้อมูลข้อสอบได้ กรุณาลองใหม่อีกครั้ง');
        }
    }

    static attachEventListeners() {
        // Quiz selection change
        document.getElementById('quizSelect').addEventListener('change', () => this.handleQuizSelection());
        
        // Student form submission
        document.getElementById('studentForm').addEventListener('submit', (e) => this.handleFormSubmit(e));
        
        // Navigation buttons
        document.getElementById('prevBtn')?.addEventListener('click', () => this.previousQuestion());
        document.getElementById('nextBtn')?.addEventListener('click', () => this.nextQuestion());
    }

    static async handleQuizSelection() {
        const quizId = document.getElementById('quizSelect').value;
        
        if (!quizId) {
            document.getElementById('totalQuestions').textContent = '-';
            document.getElementById('quizDuration').textContent = '-';
            document.getElementById('totalPoints').textContent = '-';
            return;
        }

        try {
            if (!QuizState.quizData[quizId]) {
                document.getElementById('totalQuestions').textContent = 'กำลังโหลด...';
                const quizInfo = QuizState.quizConfig.quizzes.find(q => q.id === quizId);
                QuizState.quizData[quizId] = await QuizDataLoader.loadQuizData(quizInfo);
            }

            QuizUI.updateQuizInfo(QuizState.quizData[quizId]);
        } catch (error) {
            console.error('Error loading quiz info:', error);
            alert('โหลดข้อสอบไม่สำเร็จ');
            document.getElementById('totalQuestions').textContent = '-';
        }
    }

    static handleFormSubmit(event) {
        event.preventDefault();
        
        const studentId = document.getElementById('studentId').value;
        const studentName = document.getElementById('studentName').value;
        const quizId = document.getElementById('quizSelect').value;

        if (!quizId || !QuizState.quizData[quizId]) {
            alert('กรุณาเลือกข้อสอบ');
            return;
        }

        QuizState.studentInfo = { studentId, studentName, quizId };
        QuizState.currentQuiz = QuizState.quizData[quizId];
        QuizState.userAnswers = new Array(QuizState.currentQuiz.questions.length).fill(null);

        QuizUI.showScreen('loading');
        setTimeout(() => this.startQuiz(), 1000);
    }

    static startQuiz() {
        QuizUI.showScreen('quizContainer');
        
        QuizState.quizStartTime = new Date();
        QuizState.currentQuestionIndex = 0;
        
        QuizTimer.start(QuizState.currentQuiz.duration);
        QuizUI.displayQuestion(QuizState.currentQuiz, QuizState.currentQuestionIndex, QuizState.userAnswers);
        QuizNavigator.create();
        AntiCheatSystem.initialize();
    }

    static selectAnswer(index) {
        QuizState.userAnswers[QuizState.currentQuestionIndex] = index;
        
        document.querySelectorAll('.answer-option').forEach((element, i) => {
            if (i === index) {
                element.classList.add('selected');
                element.querySelector('input').checked = true;
            } else {
                element.classList.remove('selected');
            }
        });
        
        QuizNavigator.updateNavigator();
    }

    static previousQuestion() {
        if (QuizState.currentQuestionIndex > 0) {
            QuizState.currentQuestionIndex--;
            QuizUI.displayQuestion(QuizState.currentQuiz, QuizState.currentQuestionIndex, QuizState.userAnswers);
            QuizNavigator.updateNavigator();
        }
    }

    static nextQuestion() {
        if (QuizState.currentQuestionIndex < QuizState.currentQuiz.questions.length - 1) {
            QuizState.currentQuestionIndex++;
            QuizUI.displayQuestion(QuizState.currentQuiz, QuizState.currentQuestionIndex, QuizState.userAnswers);
            QuizNavigator.updateNavigator();
        }
    }

    static confirmSubmit() {
        const answeredCount = QuizState.userAnswers.filter(a => a !== null && a !== '').length;
        document.getElementById('answeredCount').textContent = answeredCount;
        document.getElementById('totalQuestionsModal').textContent = QuizState.currentQuiz.questions.length;
        document.getElementById('submitModal').classList.add('active');
    }

    static closeSubmitModal() {
        document.getElementById('submitModal').classList.remove('active');
    }

    static submitQuiz() {
        this.closeSubmitModal();
        QuizTimer.stop();

        const endTime = new Date();
        const usedMs = endTime - QuizState.quizStartTime;
        const usedMin = Math.floor(usedMs / 60000);
        const usedSec = Math.floor((usedMs % 60000) / 1000);

        // Calculate results
        const results = GradingSystem.calculateResults(QuizState.currentQuiz, QuizState.userAnswers);
        results.timeUsed = `${usedMin} นาที ${usedSec.toString().padStart(2, '0')} วินาที`;

        // Show results screen
        QuizUI.showScreen('quizResults');
        QuizUI.displayResults(QuizState.currentQuiz, QuizState.studentInfo, results);
        AnswerReview.display(QuizState.currentQuiz, QuizState.userAnswers);

        // Prepare and save results
        const resultsToSave = {
            studentId: QuizState.studentInfo.studentId,
            studentName: QuizState.studentInfo.studentName,
            quizId: QuizState.studentInfo.quizId,
            quizTitle: QuizState.currentQuiz.title,
            score: results.earned,
            totalPoints: results.totalPoints,
            percentage: results.percentage,
            grade: results.grade,
            timeUsed: results.timeUsed,
            timestamp: new Date().toISOString(),
            answers: QuizState.currentQuiz.questions.map((q, idx) => ({
                questionId: q.id != null ? String(q.id) : `q${idx + 1}`,
                question: q.question,
                userAnswer: QuizState.userAnswers[idx],
                correctAnswer: q.correctAnswer ?? null,
                isCorrect: (q.type === 'multiple-choice') && (QuizState.userAnswers[idx] === q.correctAnswer),
                type: q.type
            }))
        };

        ResultsSaver.save(resultsToSave);
        AntiCheatSystem.cleanup();
    }
}

// ========== INITIALIZE ON DOM READY ==========
document.addEventListener('DOMContentLoaded', () => {
    QuizController.initialize();
});

// Make necessary functions globally accessible for inline event handlers
window.previousQuestion = () => QuizController.previousQuestion();
window.nextQuestion = () => QuizController.nextQuestion();
window.confirmSubmit = () => QuizController.confirmSubmit();
window.closeSubmitModal = () => QuizController.closeSubmitModal();
window.submitQuiz = () => QuizController.submitQuiz();
