#!/usr/bin/env python3
"""
Safe template conversion script - uses targeted replacements instead of large regex
Converts teaching HTML files to match 819605 template structure
"""

import os
import re

def safe_convert_720201():
    """Safely convert 720201 to match 819605 template"""
    
    file_path = os.path.join(os.path.dirname(__file__), '720201-B1-1-2568.html')
    
    print(f"\n{'='*60}")
    print(f"Converting: 720201-B1-1-2568.html")
    print(f"{'='*60}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    content = ''.join(lines)
    original_size = len(content)
    
    # 1. Fix style section - find and replace just the style tags
    content = re.sub(
        r'(<style>)[\s\S]*?(</style>)',
        r'\1\n\n    \2',
        content,
        count=1
    )
    
    # 2. Add onclick to sidebar menu links - do one by one
    menu_replacements = [
        ('href="#announcements" class="menu-link active"', 
         'href="#announcements" class="menu-link active" onclick="showSection(\'announcements\', event)"'),
        ('href="#description" class="menu-link"', 
         'href="#description" class="menu-link" onclick="showSection(\'description\', event)"'),
        ('href="#objectives" class="menu-link"', 
         'href="#objectives" class="menu-link" onclick="showSection(\'objectives\', event)"'),
        ('href="#materials" class="menu-link"', 
         'href="#materials" class="menu-link" onclick="showSection(\'materials\', event)"'),
        ('href="#schedule" class="menu-link"', 
         'href="#schedule" class="menu-link" onclick="showSection(\'schedule\', event)"'),
        ('href="#grading" class="menu-link"', 
         'href="#grading" class="menu-link" onclick="showSection(\'grading\', event)"'),
        ('href="#homework" class="menu-link"', 
         'href="#homework" class="menu-link" onclick="showSection(\'homework\', event)"'),
        ('href="#exams" class="menu-link"', 
         'href="#exams" class="menu-link" onclick="showSection(\'exams\', event)"'),
    ]
    
    for old, new in menu_replacements:
        content = content.replace(old, new)
    
    # 3. Check if showSection function already exists
    if 'function showSection(' not in content:
        # Add showSection function right after existing JavaScript starts
        showsection_func = '''        // Section Navigation with Fade-in Effect
        function showSection(sectionId, event) {
            if (event) {
                event.preventDefault();
            }

            // Hide all sections with slight delay for smooth transition
            const sections = document.querySelectorAll('.content-section');
            sections.forEach(section => {
                section.classList.remove('active');
            });

            // Show selected section with optimized timing
            requestAnimationFrame(() => {
                const targetSection = document.getElementById(sectionId);
                if (targetSection) {
                    targetSection.classList.add('active');
                }
            });

            // Update active menu item
            const menuLinks = document.querySelectorAll('.menu-link');
            menuLinks.forEach(link => {
                link.classList.remove('active');
            });
            event?.target?.closest('.menu-link')?.classList.add('active');

            // Scroll to top of content on mobile with faster animation
            if (window.innerWidth <= 1024) {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }

            // Update URL hash without scrolling
            history.pushState(null, null, `#${sectionId}`);
        }

        '''
        
        # Insert before trackPageVisit or toggleSidebar function
        content = content.replace('        // Page visit counter\n        function trackPageVisit()',
                                   showsection_func + '// Page visit counter\n        function trackPageVisit()')
    
    # 4. Check if loadSectionFromHash function exists
    if 'function loadSectionFromHash(' not in content:
        loadhash_func = '''
        // Load section from URL hash on page load
        function loadSectionFromHash() {
            const hash = window.location.hash.slice(1);
            if (hash) {
                const targetLink = document.querySelector(`.menu-link[href="#${hash}"]`);
                if (targetLink) {
                    targetLink.click();
                }
            }
        }
'''
        # Insert after toggleSidebar function
        content = content.replace('        }\n\n        // Link click tracking',
                                   '        }' + loadhash_func + '\n        // Link click tracking')
    
    # 5. Update DOMContentLoaded to include loadSectionFromHash
    if 'loadSectionFromHash();' not in content:
        old_init = '''        // Initialize tracking when page loads
        document.addEventListener('DOMContentLoaded', function() {
            trackPageVisit();'''
        
        new_init = '''        // Initialize tracking when page loads
        document.addEventListener('DOMContentLoaded', function() {
            // trackPageVisit();
            loadSectionFromHash();'''
        
        if old_init in content:
            content = content.replace(old_init, new_init)
    
    # 6. Add hashchange listener if not present
    if 'hashchange' not in content:
        listener_code = '''
            // Handle back/forward navigation
            window.addEventListener('hashchange', loadSectionFromHash);

            // Smooth scroll for internal links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    // Let the showSection function handle the navigation
                });
            });'''
        
        # Find the closing of addEventListener and add before it
        content = content.replace('        });', listener_code + '\n        });', 1)
    
    new_size = len(content)
    
    # Safety check - make sure we didn't destroy the file
    if new_size < original_size * 0.5:
        print("❌ ERROR: File size reduced by more than 50%! Aborting.")
        return False
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 720201 converted successfully")
    print(f"   Original: {original_size} bytes → New: {new_size} bytes")
    return True

def safe_convert_725103():
    """Safely convert 725103 to match 819605 template"""
    
    file_path = os.path.join(os.path.dirname(__file__), '725103-2-2568.html')
    
    print(f"\n{'='*60}")
    print(f"Converting: 725103-2-2568.html")
    print(f"{'='*60}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    content = ''.join(lines)
    original_size = len(content)
    
    # 1. Fix style section
    content = re.sub(
        r'(<style>)[\s\S]*?(</style>)',
        r'\1\n\n    \2',
        content,
        count=1
    )
    
    # 2. Add onclick to sidebar menu links
    menu_replacements = [
        ('href="#overview" class="menu-link active"', 
         'href="#overview" class="menu-link active" onclick="showSection(\'overview\', event)"'),
        ('href="#description" class="menu-link"', 
         'href="#description" class="menu-link" onclick="showSection(\'description\', event)"'),
        ('href="#materials" class="menu-link"', 
         'href="#materials" class="menu-link" onclick="showSection(\'materials\', event)"'),
        ('href="#clos" class="menu-link"', 
         'href="#clos" class="menu-link" onclick="showSection(\'clos\', event)"'),
        ('href="#mapping" class="menu-link"', 
         'href="#mapping" class="menu-link" onclick="showSection(\'mapping\', event)"'),
        ('href="#assessment" class="menu-link"', 
         'href="#assessment" class="menu-link" onclick="showSection(\'assessment\', event)"'),
        ('href="#policies" class="menu-link"', 
         'href="#policies" class="menu-link" onclick="showSection(\'policies\', event)"'),
        ('href="#schedule" class="menu-link"', 
         'href="#schedule" class="menu-link" onclick="showSection(\'schedule\', event)"'),
        ('href="#grading" class="menu-link"', 
         'href="#grading" class="menu-link" onclick="showSection(\'grading\', event)"'),
        ('href="#homework" class="menu-link"', 
         'href="#homework" class="menu-link" onclick="showSection(\'homework\', event)"'),
        ('href="#exams" class="menu-link"', 
         'href="#exams" class="menu-link" onclick="showSection(\'exams\', event)"'),
    ]
    
    for old, new in menu_replacements:
        content = content.replace(old, new)
    
    # 3. Check if showSection function already exists
    if 'function showSection(' not in content:
        showsection_func = '''        // Section Navigation with Fade-in Effect
        function showSection(sectionId, event) {
            if (event) {
                event.preventDefault();
            }

            // Hide all sections with slight delay for smooth transition
            const sections = document.querySelectorAll('.content-section');
            sections.forEach(section => {
                section.classList.remove('active');
            });

            // Show selected section with optimized timing
            requestAnimationFrame(() => {
                const targetSection = document.getElementById(sectionId);
                if (targetSection) {
                    targetSection.classList.add('active');
                }
            });

            // Update active menu item
            const menuLinks = document.querySelectorAll('.menu-link');
            menuLinks.forEach(link => {
                link.classList.remove('active');
            });
            event?.target?.closest('.menu-link')?.classList.add('active');

            // Scroll to top of content on mobile with faster animation
            if (window.innerWidth <= 1024) {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }

            // Update URL hash without scrolling
            history.pushState(null, null, `#${sectionId}`);
        }

        '''
        
        # Insert before tryLoadOBE or trackPageVisit function  
        if 'function tryLoadOBE()' in content:
            content = content.replace('        async function tryLoadOBE()',
                                       showsection_func + 'async function tryLoadOBE()')
        else:
            content = content.replace('        function trackPageVisit()',
                                       showsection_func + 'function trackPageVisit()')
    
    # 4. Check if loadSectionFromHash function exists
    if 'function loadSectionFromHash(' not in content:
        loadhash_func = '''
        // Load section from URL hash on page load
        function loadSectionFromHash() {
            const hash = window.location.hash.slice(1);
            if (hash) {
                const targetLink = document.querySelector(`.menu-link[href="#${hash}"]`);
                if (targetLink) {
                    targetLink.click();
                }
            }
        }
'''
        # Insert after toggleSidebar function
        content = content.replace('        }\n\n        // Link click tracking',
                                   '        }' + loadhash_func + '\n        // Link click tracking')
        # Or after tryLoadOBE if Link click tracking doesn't exist
        if '        }' + loadhash_func not in content:
            content = content.replace('        }\n        // Page visit counter',
                                       '        }' + loadhash_func + '\n        // Page visit counter')
    
    # 5. Update DOMContentLoaded to include loadSectionFromHash
    if 'loadSectionFromHash();' not in content:
        old_patterns = [
            ('        document.addEventListener(\'DOMContentLoaded\', function() {\n            trackPageVisit();',
             '        document.addEventListener(\'DOMContentLoaded\', function() {\n            // trackPageVisit();\n            loadSectionFromHash();'),
            ('        document.addEventListener(\'DOMContentLoaded\', function() {\n            // trackPageVisit();',
             '        document.addEventListener(\'DOMContentLoaded\', function() {\n            // trackPageVisit();\n            loadSectionFromHash();'),
        ]
        
        for old, new in old_patterns:
            if old in content:
                content = content.replace(old, new)
                break
    
    # 6. Add hashchange listener if not present
    if 'hashchange' not in content:
        listener_code = '''
            // Handle back/forward navigation
            window.addEventListener('hashchange', loadSectionFromHash);

            // Smooth scroll for internal links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    // Let the showSection function handle the navigation
                });
            });'''
        
        # Add before the closing of addEventListener
        # Look for the pattern before tryLoadOBE call
        if 'tryLoadOBE();' in content:
            content = content.replace(
                '            // Attempt to load JSON data if available\n            tryLoadOBE();',
                '            loadSectionFromHash();\n            tryLoadOBE();' + listener_code
            )
        else:
            content = content.replace('        });', listener_code + '\n        });', 1)
    
    new_size = len(content)
    
    # Safety check
    if new_size < original_size * 0.5:
        print("❌ ERROR: File size reduced by more than 50%! Aborting.")
        return False
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 725103 converted successfully")
    print(f"   Original: {original_size} bytes → New: {new_size} bytes")
    return True

def main():
    print("\n" + "="*60)
    print("SAFE Template Conversion - Targeted Replacements Only")
    print("="*60)
    
    success_count = 0
    
    if safe_convert_720201():
        success_count += 1
    
    if safe_convert_725103():
        success_count += 1
    
    print("\n" + "="*60)
    if success_count == 2:
        print("✅ All files converted successfully!")
        print("="*60)
        print("\nChanges made:")
        print("1. ✅ Cleaned <style> sections")
        print("2. ✅ Added onclick handlers to menu links")
        print("3. ✅ Added showSection() function")
        print("4. ✅ Added loadSectionFromHash() function")
        print("5. ✅ Added hashchange event listener")
        print("6. ✅ Updated DOMContentLoaded initialization")
        print("\n✅ All pages now match 819605 template!")
    else:
        print(f"⚠️ Only {success_count}/2 files converted")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
