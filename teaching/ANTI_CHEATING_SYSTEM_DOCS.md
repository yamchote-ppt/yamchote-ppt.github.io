# 🔒 Anti-Cheating System - Complete Documentation

## Overview
The quiz system now has **comprehensive detection** for all types of window/application switching, including:
- ✅ Tab switching within browser
- ✅ Switching to other programs
- ✅ Clicking on other monitors
- ✅ Alt+Tab / Windows+Tab
- ✅ Minimizing window
- ✅ Virtual desktop switching

---

## 🎯 Detection Methods

### 1. **Tab Switching Detection** (`visibilitychange` event)
**Detects:**
- Switching to another browser tab
- Minimizing browser window
- Switching to different virtual desktop

**Triggers:**
- When page becomes hidden (`document.hidden === true`)

**Action:**
- Increments violation counter
- Shows warning alert
- Auto-submits after MAX_TAB_SWITCHES

---

### 2. **Window Focus Loss Detection** (`blur` event)
**Detects:**
- Clicking on another program
- Clicking on another monitor
- Alt+Tab to switch applications
- Windows+Tab to task view
- Clicking on taskbar
- Clicking outside browser window

**Triggers:**
- When browser window loses focus

**Action:**
- Increments violation counter
- Shows warning alert
- Auto-submits after MAX_TAB_SWITCHES

---

### 3. **Mouse Leave Detection** (`mouseleave` event)
**Detects:**
- Mouse cursor leaving the browser window area
- Moving to another monitor

**Triggers:**
- When mouse exits document boundaries

**Action:**
- Logs warning (monitoring only)
- Does not increment counter (too sensitive)

---

### 4. **Developer Tools Detection**
**Detects:**
- F12 key press
- Ctrl+Shift+I (Inspect)
- Ctrl+Shift+C (Inspect Element)
- Ctrl+Shift+J (Console)
- Ctrl+U (View Source)
- Window size changes (DevTools open)

**Action:**
- **Instant auto-submit** (no warnings)

---

## ⚙️ Configuration

### Adjust Strictness Level

```javascript
const MAX_TAB_SWITCHES = 2; // Current: 2 warnings allowed
```

**Recommended Settings:**

| Mode | Value | Description |
|------|-------|-------------|
| **Strict** | `0` | Instant submit on first violation |
| **Moderate** | `2` | 2 warnings before submit (current) |
| **Lenient** | `3` | 3 warnings before submit |
| **Testing** | `999` | Many warnings (for testing only) |

---

## 📊 How It Works

### Scenario 1: Student clicks on another monitor
```
1. Window 'blur' event fires
2. tabSwitchCount increases (1/2)
3. Alert shown: "คำเตือน! (1/2)"
4. Student returns to quiz
5. If happens again → (2/2) warning
6. Third time → AUTO-SUBMIT
```

### Scenario 2: Student presses Alt+Tab
```
1. Window 'blur' event fires
2. tabSwitchCount increases
3. Alert shown with remaining chances
4. If exceeds limit → AUTO-SUBMIT
```

### Scenario 3: Student switches browser tab
```
1. 'visibilitychange' event fires
2. document.hidden becomes true
3. tabSwitchCount increases
4. Alert shown
5. If exceeds limit → AUTO-SUBMIT
```

### Scenario 4: Student opens Developer Tools
```
1. Keydown event detects F12
2. Event prevented
3. INSTANT AUTO-SUBMIT (no warnings)
4. Quiz ends immediately
```

---

## 🚨 Warning Messages

### Initial Warning (on quiz start)
```
⚠️ คำเตือนสำคัญ!

📌 กฎระหว่างทำข้อสอบ:
• ห้ามเปลี่ยนแท็บหรือหน้าต่าง
• ห้ามคลิกที่โปรแกรมอื่น
• ห้ามคลิกที่จอมอนิเตอร์อื่น
• ห้ามกด Alt+Tab หรือ Windows+Tab
• ห้ามเปิด Developer Tools (F12)
• ห้ามคัดลอก/วางข้อความ

⚠️ คุณมีสิทธิ์เตือน 2 ครั้ง
หากฝ่าฝืนมากกว่านี้ ระบบจะส่งข้อสอบอัตโนมัติทันที!

✅ กรุณาอยู่ในหน้าต่างนี้ตลอดเวลาทำข้อสอบ
```

### Violation Warning (each time)
```
⚠️ คำเตือน! (1/2)

คุณได้เปลี่ยนไปใช้โปรแกรมหรือหน้าต่างอื่น
หากทำอีก 1 ครั้ง ระบบจะส่งข้อสอบอัตโนมัติ

กรุณาอยู่ในหน้านี้ตลอดเวลาทำข้อสอบ
```

### Auto-Submit Warning (final)
```
⚠️ คุณได้เปลี่ยนไปใช้โปรแกรมอื่นหรือหน้าต่างอื่นมากเกินไป
ระบบจะส่งข้อสอบของคุณอัตโนมัติ
```

### Results Page Warning
```
⚠️ ข้อสอบถูกส่งอัตโนมัติ
เหตุผล: เปลี่ยนแท็บหรือหน้าต่างมากเกินไป
อาจารย์ผู้สอนจะได้รับการแจ้งเตือน
```

---

## 📝 Activity Logging

All violations are logged to `localStorage` for instructor review:

```javascript
{
  timestamp: "2025-10-15T10:30:45.123Z",
  studentId: "6501234567",
  quizId: "demo",
  action: "tab_switch",
  details: {},
  tabSwitchCount: 2
}
```

### View Activity Log

**In Browser Console:**
```javascript
// View all activity
JSON.parse(localStorage.getItem('quizActivityLog'))

// Clear activity log
localStorage.removeItem('quizActivityLog')

// Count violations for a student
const logs = JSON.parse(localStorage.getItem('quizActivityLog'))
logs.filter(log => log.studentId === '6501234567').length
```

---

## 🧪 Testing Checklist

### Test 1: Tab Switching
- [ ] Start quiz
- [ ] Open new tab (Ctrl+T)
- [ ] Should see warning (1/2)
- [ ] Switch back
- [ ] Open new tab again
- [ ] Should see warning (2/2)
- [ ] Open new tab third time
- [ ] Should auto-submit

### Test 2: Other Program
- [ ] Start quiz
- [ ] Click on another program (e.g., Notepad)
- [ ] Should see warning (1/2)
- [ ] Click back to browser
- [ ] Repeat
- [ ] Should auto-submit after limit

### Test 3: Other Monitor
- [ ] Start quiz on Monitor 1
- [ ] Click anywhere on Monitor 2
- [ ] Should see warning
- [ ] Click back to quiz
- [ ] Repeat to trigger auto-submit

### Test 4: Alt+Tab
- [ ] Start quiz
- [ ] Press Alt+Tab
- [ ] Should see warning
- [ ] Return to quiz
- [ ] Repeat to trigger limit

### Test 5: Developer Tools
- [ ] Start quiz
- [ ] Press F12
- [ ] Should see warning and INSTANT auto-submit

### Test 6: Copy/Paste
- [ ] Start quiz
- [ ] Try to select and copy text
- [ ] Should see block message
- [ ] Try to paste
- [ ] Should see block message

### Test 7: Right-Click
- [ ] Start quiz
- [ ] Right-click on page
- [ ] Should be blocked (no context menu)

---

## 🔧 Troubleshooting

### Issue: False positives (too many auto-submits)

**Solution:** Increase MAX_TAB_SWITCHES
```javascript
const MAX_TAB_SWITCHES = 3; // More lenient
```

---

### Issue: Students complain about accidental clicks

**Solution 1:** Add grace period
```javascript
let lastBlurTime = 0;
window.addEventListener('blur', function() {
    const now = Date.now();
    // Ignore if blur was < 500ms ago (accidental)
    if (now - lastBlurTime < 500) {
        return;
    }
    lastBlurTime = now;
    // ... rest of code
});
```

**Solution 2:** Only count if away for > X seconds
```javascript
let blurStartTime = 0;
window.addEventListener('blur', function() {
    blurStartTime = Date.now();
});

window.addEventListener('focus', function() {
    const timeAway = Date.now() - blurStartTime;
    if (timeAway > 2000) { // Only count if away > 2 seconds
        tabSwitchCount++;
        // ... show warning
    }
});
```

---

### Issue: System too strict for legitimate use

**Recommendations:**
1. Set MAX_TAB_SWITCHES to 3-5 for first exam
2. Monitor activity logs
3. Adjust based on student feedback
4. Consider "calculator exception" if students need calculator

---

## 📱 Mobile/Tablet Considerations

**Current Behavior:**
- Switching apps on mobile will trigger violation
- Rotating device may trigger blur event
- Virtual keyboard may cause issues

**Recommended:**
```javascript
// Detect if mobile device
const isMobile = /Android|webOS|iPhone|iPad|iPod/i.test(navigator.userAgent);

if (isMobile) {
    MAX_TAB_SWITCHES = 5; // More lenient on mobile
}
```

---

## 🎓 Best Practices for Instructors

### Before Exam
1. ✅ Test the system yourself
2. ✅ Announce rules clearly to students
3. ✅ Demo the violation system
4. ✅ Provide practice quiz for familiarization
5. ✅ Set appropriate MAX_TAB_SWITCHES value

### During Exam
1. ✅ Monitor activity logs in real-time
2. ✅ Be available for technical issues
3. ✅ Have backup plan for system failures

### After Exam
1. ✅ Review activity logs for all students
2. ✅ Check for suspicious patterns
3. ✅ Follow up on auto-submitted quizzes
4. ✅ Gather student feedback

---

## 🔐 Security Features Summary

| Feature | Status | Strictness |
|---------|--------|------------|
| Tab Switch Detection | ✅ Enabled | Medium (2 warnings) |
| Window Blur Detection | ✅ Enabled | Medium (2 warnings) |
| Multi-Monitor Detection | ✅ Enabled | Medium (2 warnings) |
| Alt+Tab Detection | ✅ Enabled | Medium (2 warnings) |
| DevTools Detection | ✅ Enabled | High (instant) |
| Copy Prevention | ✅ Enabled | Block only |
| Paste Prevention | ✅ Enabled | Block only |
| Right-Click Block | ✅ Enabled | Block only |
| Page Reload Warning | ✅ Enabled | Warning only |
| Activity Logging | ✅ Enabled | All events |

---

## 📊 Statistics Tracking

Track effectiveness of anti-cheating system:

```javascript
// Get statistics
const logs = JSON.parse(localStorage.getItem('quizActivityLog') || '[]');

// Total violations
logs.length

// Students with violations
[...new Set(logs.map(l => l.studentId))].length

// Most common violation type
const violations = logs.map(l => l.action);
const counts = {};
violations.forEach(v => counts[v] = (counts[v] || 0) + 1);
console.log(counts);

// Auto-submitted quizzes
const results = JSON.parse(localStorage.getItem('quizResults') || '[]');
results.filter(r => r.autoSubmitted).length
```

---

## 🚀 Future Enhancements

Possible additions:
- [ ] Webcam monitoring
- [ ] Eye tracking
- [ ] Screen recording
- [ ] AI-based cheating detection
- [ ] Network activity monitoring
- [ ] Clipboard monitoring
- [ ] Screenshot detection
- [ ] Virtual machine detection

---

## 📞 Support

For issues or questions:
- Email: instructor@university.edu
- Technical Support: it-support@university.edu
- Documentation: [Link to full guide]

---

**Last Updated:** October 15, 2025  
**Version:** 2.0  
**Author:** Quiz System Development Team
