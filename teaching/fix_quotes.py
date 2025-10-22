#!/usr/bin/env python3
"""Fix incorrectly escaped quotes in onclick attributes"""
import re

files = ['720201-B1-1-2568.html', '725103-2-2568.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Fix escaped single quotes back to proper single quotes
    # From: onclick="showSection(\'xxx\', event)"
    # To:   onclick="showSection('xxx', event)"
    content = content.replace("\\'", "'")
    
    changes = len(original) - len(content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Fixed quotes in {filename}")

print("\n✅ All files fixed!")