/**
 * Quiz System Configuration
 * 819605 - Discrete Mathematics
 * Southeast Asia University
 */

const CONFIG = {
    // API Configuration
    APP_SCRIPT_URL: 'https://script.google.com/macros/s/AKfycbx3Jz0Jcqvn4_YU9OEL3IK3_pixVgMg9gyk9kWpo7m8HtAl8bFCttOcXjgQjhn0-LqbUw/exec',
    
    // Quiz Configuration
    QUIZ: {
        courseCode: '819605',
        quizDataPath: 'data/quizzes/',
        configFile: 'quiz-config.json'
    },
    
    // Anti-Cheat Configuration
    ANTI_CHEAT: {
        maxTabSwitches: 2,
        devToolsThreshold: 160,
        checkInterval: 1000
    },
    
    // Timer Configuration
    TIMER: {
        warningThreshold: 300, // 5 minutes
        updateInterval: 1000
    },
    
    // Grading Configuration
    GRADING: {
        A: 80,
        B: 70,
        C: 60,
        D: 50,
        F: 0
    }
};

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
}
