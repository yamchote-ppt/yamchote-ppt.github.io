#!/usr/bin/env python3
"""
Script to convert teaching HTML files to match 819605 template structure
Makes 720201 and 725103 follow the same pattern as 819605
"""

import os
import re

def convert_720201():
    """Convert 720201 to match 819605 template"""
    
    file_path = os.path.join(os.path.dirname(__file__), '720201-B1-1-2568.html')
    
    print(f"\n{'='*60}")
    print(f"Converting: 720201-B1-1-2568.html")
    print(f"{'='*60}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix the <style> section to match 819605 (empty style tags)
    content = re.sub(
        r'<style>.*?</style>',
        '<style>\n\n    </style>',
        content,
        flags=re.DOTALL
    )
    
    # 2. Update sidebar menu items to include onclick handlers
    sidebar_menu = '''            <h3 class="sidebar-title">📑 เนื้อหารายวิชา</h3>
            <ul class="sidebar-menu">
                <li><a href="#announcements" class="menu-link active" onclick="showSection('announcements', event)">
                    <span class="icon">📢</span>
                    <span>ประกาศ</span>
                </a></li>
                <li><a href="#description" class="menu-link" onclick="showSection('description', event)">
                    <span class="icon">📖</span>
                    <span>คำอธิบายรายวิชา</span>
                </a></li>
                <li><a href="#objectives" class="menu-link" onclick="showSection('objectives', event)">
                    <span class="icon">🎯</span>
                    <span>วัตถุประสงค์</span>
                </a></li>
                <li><a href="#materials" class="menu-link" onclick="showSection('materials', event)">
                    <span class="icon">📄</span>
                    <span>เอกสารประกอบการสอน</span>
                </a></li>
                <li><a href="#schedule" class="menu-link" onclick="showSection('schedule', event)">
                    <span class="icon">📅</span>
                    <span>ตารางสอน</span>
                </a></li>
                <li><a href="#grading" class="menu-link" onclick="showSection('grading', event)">
                    <span class="icon">📊</span>
                    <span>การประเมินผล</span>
                </a></li>
                <li><a href="#homework" class="menu-link" onclick="showSection('homework', event)">
                    <span class="icon">✏️</span>
                    <span>การบ้าน</span>
                </a></li>
                <li><a href="#exams" class="menu-link" onclick="showSection('exams', event)">
                    <span class="icon">📝</span>
                    <span>ข้อสอบ</span>
                </a></li>
            </ul>'''
    
    content = re.sub(
        r'<h3 class="sidebar-title">.*?</ul>',
        sidebar_menu,
        content,
        flags=re.DOTALL
    )
    
    # 3. Replace JavaScript section with 819605 template
    js_section = '''    <!-- JavaScript -->
    <script>
        // Section Navigation with Fade-in Effect
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

        // Toggle Sidebar on Mobile
        function toggleSidebar() {
            const sidebar = document.getElementById('sidebar');
            sidebar.classList.toggle('collapsed');
        }

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

        // Page visit counter
        function trackPageVisit() {
            const pageKey = 'page_visits_720201';
            let visits = parseInt(localStorage.getItem(pageKey) || '0');
            visits++;
            localStorage.setItem(pageKey, visits.toString());
            console.log(`Page visits: ${visits}`);
        }

        // Initialize on page load
        document.addEventListener('DOMContentLoaded', function() {
            // trackPageVisit();
            loadSectionFromHash();

            // Handle back/forward navigation
            window.addEventListener('hashchange', loadSectionFromHash);

            // Smooth scroll for internal links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    // Let the showSection function handle the navigation
                });
            });
        });
    </script>'''
    
    # Find and replace the entire script section
    content = re.sub(
        r'<!-- Simple Analytics Script -->.*?</script>',
        js_section,
        content,
        flags=re.DOTALL
    )
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 720201 converted successfully")

def convert_725103():
    """Convert 725103 to match 819605 template"""
    
    file_path = os.path.join(os.path.dirname(__file__), '725103-2-2568.html')
    
    print(f"\n{'='*60}")
    print(f"Converting: 725103-2-2568.html")
    print(f"{'='*60}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix the <style> section to match 819605 (empty style tags)
    content = re.sub(
        r'<style>.*?</style>',
        '<style>\n\n    </style>',
        content,
        flags=re.DOTALL
    )
    
    # 2. Update sidebar menu items to include onclick handlers
    sidebar_menu = '''            <h3 class="sidebar-title">📑 เนื้อหารายวิชา</h3>
            <ul class="sidebar-menu">
                <li><a href="#overview" class="menu-link active" onclick="showSection('overview', event)">
                    <span class="icon">🏠</span>
                    <span>ภาพรวมรายวิชา</span>
                </a></li>
                <li><a href="#description" class="menu-link" onclick="showSection('description', event)">
                    <span class="icon">📖</span>
                    <span>คำอธิบายรายวิชา</span>
                </a></li>
                <li><a href="#materials" class="menu-link" onclick="showSection('materials', event)">
                    <span class="icon">📄</span>
                    <span>เอกสารประกอบการสอน</span>
                </a></li>
                <li><a href="#clos" class="menu-link" onclick="showSection('clos', event)">
                    <span class="icon">🎯</span>
                    <span>ผลลัพธ์การเรียนรู้ (CLOs)</span>
                </a></li>
                <li><a href="#mapping" class="menu-link" onclick="showSection('mapping', event)">
                    <span class="icon">🧩</span>
                    <span>การแมป CLO-PLO</span>
                </a></li>
                <li><a href="#assessment" class="menu-link" onclick="showSection('assessment', event)">
                    <span class="icon">🧪</span>
                    <span>แผนการประเมินผล</span>
                </a></li>
                <li><a href="#policies" class="menu-link" onclick="showSection('policies', event)">
                    <span class="icon">📜</span>
                    <span>นโยบายรายวิชา</span>
                </a></li>
                <li><a href="#schedule" class="menu-link" onclick="showSection('schedule', event)">
                    <span class="icon">📅</span>
                    <span>ตารางสอน</span>
                </a></li>
                <li><a href="#grading" class="menu-link" onclick="showSection('grading', event)">
                    <span class="icon">📊</span>
                    <span>การประเมินผล</span>
                </a></li>
                <li><a href="#homework" class="menu-link" onclick="showSection('homework', event)">
                    <span class="icon">✏️</span>
                    <span>การบ้าน</span>
                </a></li>
                <li><a href="#exams" class="menu-link" onclick="showSection('exams', event)">
                    <span class="icon">📝</span>
                    <span>ข้อสอบ</span>
                </a></li>
            </ul>'''
    
    content = re.sub(
        r'<h3 class="sidebar-title">.*?</ul>',
        sidebar_menu,
        content,
        flags=re.DOTALL
    )
    
    # 3. Replace JavaScript section with 819605 template (keeping 725103 page key)
    js_section = '''    <!-- JavaScript -->
    <script>
        // Section Navigation with Fade-in Effect
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

        // Toggle Sidebar on Mobile
        function toggleSidebar() {
            const sidebar = document.getElementById('sidebar');
            sidebar.classList.toggle('collapsed');
        }

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

        // JSON-driven OBE loader (loads from data/725103-obe.json)
        async function tryLoadOBE() {
            try {
                console.log('Attempting to load JSON from: data/725103-obe.json');
                const res = await fetch('data/725103-obe.json', { cache: 'no-store' });
                console.log('Fetch response status:', res.status, res.ok);
                if (!res.ok) {
                    console.log('JSON file not found or error loading - using default content');
                    return;
                }
                const data = await res.json();
                console.log('JSON data loaded successfully:', data);

                // Populate Schedule (if available)
                if (Array.isArray(data.schedule)) {
                    const list = document.getElementById('schedule-list');
                    const ph = document.getElementById('schedule-placeholder');
                    if (list) {
                        list.innerHTML = '';
                        for (const s of data.schedule) {
                            const div = document.createElement('div');
                            div.className = 'schedule-item';
                            const materials = Array.isArray(s.materials) ? `
                                <ul>
                                    ${s.materials.map(m => `<li><a href="${m.href}" target="_blank">${m.label}</a></li>`).join('')}
                                </ul>` : '';
                            div.innerHTML = `
                                <strong>${s.week || ''}${s.date ? ' ('+s.date+')' : ''}</strong>
                                <p>${s.topic || ''}${s.notes ? '<br><small style="color: var(--gray-700);">'+s.notes+'</small>' : ''}</p>
                                ${materials}
                            `;
                            list.appendChild(div);
                        }
                        if (ph) ph.style.display = 'none';
                    }
                }
                console.log('All data populated successfully!');
            } catch (err) {
                console.error('Error loading OBE data:', err);
            }
        }

        // Page visit counter
        function trackPageVisit() {
            const pageKey = 'page_visits_725103';
            let visits = parseInt(localStorage.getItem(pageKey) || '0');
            visits++;
            localStorage.setItem(pageKey, visits.toString());
            console.log(`Page visits: ${visits}`);
        }

        // Initialize on page load
        document.addEventListener('DOMContentLoaded', function() {
            // trackPageVisit();
            loadSectionFromHash();
            tryLoadOBE();

            // Handle back/forward navigation
            window.addEventListener('hashchange', loadSectionFromHash);

            // Smooth scroll for internal links
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    // Let the showSection function handle the navigation
                });
            });
        });
    </script>'''
    
    # Find and replace the entire script section - need to handle the longer script in 725103
    content = re.sub(
        r'<script>.*?</script>\s*</div> <!-- End main-layout -->',
        js_section + '\n    </div> <!-- End main-layout -->',
        content,
        flags=re.DOTALL
    )
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ 725103 converted successfully")

def main():
    print("\n" + "="*60)
    print("Converting teaching pages to match 819605 template")
    print("="*60)
    
    convert_720201()
    convert_725103()
    
    print("\n" + "="*60)
    print("✅ All files converted successfully!")
    print("="*60)
    print("\nChanges made:")
    print("1. ✅ Cleaned <style> sections (empty tags matching 819605)")
    print("2. ✅ Added onclick='showSection(...)' to all menu links")
    print("3. ✅ Added showSection() JavaScript function")
    print("4. ✅ Added loadSectionFromHash() function")
    print("5. ✅ Added hashchange event listener")
    print("6. ✅ Added smooth scroll handling")
    print("\nAll pages now follow 819605 template structure!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
