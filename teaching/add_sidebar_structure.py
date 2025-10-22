#!/usr/bin/env python3
"""
Script to add sidebar navigation structure to teaching HTML files
Converts from main-container layout to main-layout with sidebar
"""

import os
import re

def add_sidebar_to_720201(file_path):
    """Add sidebar structure to 720201 file"""
    
    print(f"\n{'='*60}")
    print(f"Processing: {file_path}")
    print(f"{'='*60}")
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Sidebar HTML for 720201
    sidebar_html = '''    <!-- Main Layout -->
    <div class="main-layout">
        <!-- Left Sidebar Navigation -->
        <aside class="sidebar" id="sidebar">
            <h3 class="sidebar-title">📑 เนื้อหารายวิชา</h3>
            <ul class="sidebar-menu">
                <li><a href="#announcements" class="menu-link active">
                    <span class="icon">📢</span>
                    <span>ประกาศ</span>
                </a></li>
                <li><a href="#description" class="menu-link">
                    <span class="icon">📖</span>
                    <span>คำอธิบายรายวิชา</span>
                </a></li>
                <li><a href="#objectives" class="menu-link">
                    <span class="icon">🎯</span>
                    <span>วัตถุประสงค์</span>
                </a></li>
                <li><a href="#materials" class="menu-link">
                    <span class="icon">📄</span>
                    <span>เอกสารประกอบการสอน</span>
                </a></li>
                <li><a href="#schedule" class="menu-link">
                    <span class="icon">📅</span>
                    <span>ตารางสอน</span>
                </a></li>
                <li><a href="#grading" class="menu-link">
                    <span class="icon">📊</span>
                    <span>การประเมินผล</span>
                </a></li>
                <li><a href="#homework" class="menu-link">
                    <span class="icon">✏️</span>
                    <span>การบ้าน</span>
                </a></li>
                <li><a href="#exams" class="menu-link">
                    <span class="icon">📝</span>
                    <span>ข้อสอบ</span>
                </a></li>
            </ul>
        </aside>

        <!-- Main Content Area -->
        <main class="content-area">'''
    
    # Replace main-container with sidebar structure
    pattern = r'    <!-- Main Content -->\s*<main class="main-container">'
    replacement = sidebar_html
    
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
        
        # Also need to close the div.main-layout at the end
        # Find the closing </body> and add closing div before it
        content = content.replace('</body>', '    </div> <!-- End main-layout -->\n</body>')
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Sidebar structure added successfully")
        return True
    else:
        print("⚠️ Pattern not found - file may already have sidebar")
        return False

def add_sidebar_to_725103(file_path):
    """Add sidebar structure to 725103 file"""
    
    print(f"\n{'='*60}")
    print(f"Processing: {file_path}")
    print(f"{'='*60}")
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Sidebar HTML for 725103
    sidebar_html = '''    <!-- Main Layout -->
    <div class="main-layout">
        <!-- Left Sidebar Navigation -->
        <aside class="sidebar" id="sidebar">
            <h3 class="sidebar-title">📑 เนื้อหารายวิชา</h3>
            <ul class="sidebar-menu">
                <li><a href="#overview" class="menu-link active">
                    <span class="icon">🏠</span>
                    <span>ภาพรวมรายวิชา</span>
                </a></li>
                <li><a href="#description" class="menu-link">
                    <span class="icon">📖</span>
                    <span>คำอธิบายรายวิชา</span>
                </a></li>
                <li><a href="#materials" class="menu-link">
                    <span class="icon">📄</span>
                    <span>เอกสารประกอบการสอน</span>
                </a></li>
                <li><a href="#clos" class="menu-link">
                    <span class="icon">🎯</span>
                    <span>ผลลัพธ์การเรียนรู้ (CLOs)</span>
                </a></li>
                <li><a href="#mapping" class="menu-link">
                    <span class="icon">🧩</span>
                    <span>การแมป CLO-PLO</span>
                </a></li>
                <li><a href="#assessment" class="menu-link">
                    <span class="icon">🧪</span>
                    <span>แผนการประเมินผล</span>
                </a></li>
                <li><a href="#policies" class="menu-link">
                    <span class="icon">📜</span>
                    <span>นโยบายรายวิชา</span>
                </a></li>
                <li><a href="#schedule" class="menu-link">
                    <span class="icon">📅</span>
                    <span>ตารางสอน</span>
                </a></li>
                <li><a href="#grading" class="menu-link">
                    <span class="icon">📊</span>
                    <span>การประเมินผล</span>
                </a></li>
                <li><a href="#homework" class="menu-link">
                    <span class="icon">✏️</span>
                    <span>การบ้าน</span>
                </a></li>
                <li><a href="#exams" class="menu-link">
                    <span class="icon">📝</span>
                    <span>ข้อสอบ</span>
                </a></li>
            </ul>
        </aside>

        <!-- Main Content Area -->
        <main class="content-area">'''
    
    # Replace main-container with sidebar structure
    pattern = r'    <!-- Main Content -->\s*<main class="main-container">'
    replacement = sidebar_html
    
    if re.search(pattern, content):
        content = re.sub(pattern, replacement, content)
        
        # Also need to close the div.main-layout at the end
        # Find the closing </body> and add closing div before it
        content = content.replace('</body>', '    </div> <!-- End main-layout -->\n</body>')
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Sidebar structure added successfully")
        return True
    else:
        print("⚠️ Pattern not found - file may already have sidebar")
        return False

def main():
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Files to process
    files_to_process = [
        {
            'path': os.path.join(script_dir, '720201-B1-1-2568.html'),
            'function': add_sidebar_to_720201
        },
        {
            'path': os.path.join(script_dir, '725103-2-2568.html'),
            'function': add_sidebar_to_725103
        }
    ]
    
    success_count = 0
    
    for file_info in files_to_process:
        file_path = file_info['path']
        process_func = file_info['function']
        
        if os.path.exists(file_path):
            if process_func(file_path):
                success_count += 1
        else:
            print(f"\n⚠️ File not found: {file_path}")
    
    print(f"\n{'='*60}")
    print(f"✅ Successfully updated: {success_count}/{len(files_to_process)} files")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
