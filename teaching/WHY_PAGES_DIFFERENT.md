# Why Each Page Looks Different - Explanation

## TL;DR
The pages have **intentionally different layouts**:
- **819605** & **720201**: Sidebar navigation layout
- **725103**: Simple single-column layout (no sidebar)

The embedded styles in each HTML file are **overriding** the common CSS, which is why they look different even though they all link to `common-styles.css`.

## The Root Cause

### CSS Cascade Order
```
1. Browser defaults
2. common-styles.css (external file) ← Loaded first
3. <style> in HTML (embedded) ← Loaded second, OVERRIDES common-styles.css
4. Inline styles
```

Since the `<style>` tags come **after** the `<link>` tag, all embedded styles override the common CSS!

## Current State

### 819605-2-2568.html (Discrete Mathematics) ✅
```html
<link rel="stylesheet" href="common-styles.css">
<style>
    /* Only 20 lines of page-specific styles */
    /* Scrollbar customization only */
</style>
```
**Status:** ✅ Using common CSS properly - looks clean!

### 725103-2-2568.html (Data Structure) ❌
```html
<link rel="stylesheet" href="common-styles.css">
<style>
    /* 400+ lines of FULL CSS */
    /* Completely overrides common-styles.css */
</style>
```
**Status:** ❌ Embedded styles override everything!

### 720201-B1-1-2568.html (Quantitative Analysis) ❌
```html
<link rel="stylesheet" href="common-styles.css">
<style>
    /* 500+ lines of FULL CSS */
    /* Completely overrides common-styles.css */
</style>
```
**Status:** ❌ Embedded styles override everything!

## Layout Differences

### Sidebar Layout (819605, 720201)
```
┌─────────────────────────────────────┐
│         Top Navigation Bar          │
├──────────┬──────────────────────────┤
│ Sidebar  │   Main Content Area      │
│  Menu    │                          │
│  📚      │   Content goes here...   │
│  📊      │                          │
│  📝      │                          │
└──────────┴──────────────────────────┘
```
Uses: `.main-layout` with `.sidebar` and `.content-area`

### Simple Layout (725103)
```
┌─────────────────────────────────────┐
│         Top Navigation Bar          │
├─────────────────────────────────────┤
│                                     │
│        Main Content Area            │
│     (full width, no sidebar)        │
│                                     │
│     Content goes here...            │
│                                     │
└─────────────────────────────────────┘
```
Uses: `.main-container` (single column)

## The Solution

### Option 1: Quick Fix (Recommended)
**Remove duplicate embedded styles, keep only layout-specific code**

For **725103-2-2568.html**, replace 400+ lines with:
```html
<style>
    /* Page-specific: Simple layout (no sidebar) */
    .main-container {
        max-width: 1200px;
        margin: 2rem auto;
        padding: 0 2rem;
    }
</style>
```

For **720201-B1-1-2568.html**, replace 500+ lines with:
```html
<style>
    /* Page-specific: Sidebar layout */
    :root {
        --sidebar-width: 270px;
    }
    
    .main-layout {
        display: flex;
    }
    
    .sidebar {
        width: var(--sidebar-width);
    }
    
    .content-area {
        flex: 1;
        min-width: 0;
    }
    
    /* Scrollbar styling */
    .sidebar::-webkit-scrollbar {
        width: 6px;
    }
    /* ... scrollbar styles ... */
</style>
```

### Option 2: Update common-styles.css (Better Long-term)
**Add support for both layouts in the common CSS file**

Add to `common-styles.css`:
```css
/* ============================================================
   LAYOUT VARIATIONS
   ============================================================ */

/* Sidebar Layout (for pages with navigation menu) */
.main-layout {
    max-width: 1400px;
    margin: 2rem auto;
    padding: 0 2rem;
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 2rem;
}

/* Simple Layout (for pages without sidebar) */
.main-container {
    max-width: 1200px;
    margin: 2rem auto;
    padding: 0 2rem;
}
```

Then **remove all duplicate styles** from HTML files!

## Implementation Plan

### Step 1: Backup Files ✅
Already have: `*-backup.html` files

### Step 2: Clean Up 725103-2-2568.html
Remove lines 32-550 (embedded CSS), keep only:
- Page layout type identifier
- Any truly unique page styles

### Step 3: Clean Up 720201-B1-1-2568.html
Remove lines 32-550 (embedded CSS), keep only:
- Sidebar-specific styles
- Scrollbar customization

### Step 4: Update common-styles.css (Optional)
Add layout variation support for future pages

### Step 5: Test All Pages
- Open all 3 pages in browser
- Verify layouts render correctly
- Check responsive design
- Verify no broken elements

## Why This Happened

1. **Initial approach**: Added `<link>` tag but kept all embedded styles
2. **CSS Cascade**: Embedded styles override external stylesheet
3. **Result**: Pages still use their old embedded styles, ignoring common-styles.css

## Benefits After Fix

✅ **Consistency**: All pages use same base styles  
✅ **Maintainability**: Edit one CSS file instead of three  
✅ **Performance**: Browser caches common CSS  
✅ **Flexibility**: Each page can still have unique layout  
✅ **File Size**: HTML files ~400-500 lines smaller  

## Quick Command

To see how much CSS is embedded in each file:
```powershell
Get-Content "725103-2-2568.html" | Select-String "<style>" -Context 1,10
```

## Next Actions

1. **Review this document** - Understand the issue
2. **Choose Option 1 or 2** - Quick fix or comprehensive update
3. **Apply changes** - Clean up embedded CSS
4. **Test thoroughly** - Verify all pages work
5. **Document** - Update COMMON_CSS_GUIDE.md with layout variations

---

**Root Cause:** Embedded `<style>` overrides external CSS  
**Impact:** Pages look completely different despite linking to common CSS  
**Fix:** Remove duplicate styles, keep only layout-specific code  
**Priority:** High (defeats purpose of common CSS)
