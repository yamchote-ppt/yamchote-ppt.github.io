#!/usr/bin/env python3
"""Fix duplicate onclick attributes"""
import re

files = ['720201-B1-1-2568.html', '725103-2-2568.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Remove duplicate onclick attributes - match the full pattern including quotes and escaped quotes
    content = re.sub(r'onclick="showSection\(\'([^\']+)\', event\)" onclick="showSection\(\'([^\']+)\', event\)"', 
                     r'onclick="showSection(\'\1\', event)"', content)
    
    changes = len(original) - len(content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Fixed duplicates in {filename} (removed {changes} bytes)")

print("\n✅ All files fixed!")
