"""
Script to update teaching HTML files to use common CSS
This will add the common-styles.css link and remove duplicate embedded styles
"""

import re
import os

def update_html_file(file_path):
    """Update a single HTML file to use common CSS"""
    print(f"\n{'='*60}")
    print(f"Processing: {file_path}")
    print('='*60)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False
    
    # Check if already updated
    if 'common-styles.css' in content:
        print("✅ File already references common-styles.css")
        return True
    
    # Pattern to find the embedded <style> section
    # We want to find from <style> to </style> but keep scrollbar styling
    style_pattern = r'(<style>)(.*?)(\/\* Scrollbar Styling \*\/.*?<\/style>)'
    
    def replace_styles(match):
        # Keep only page-specific styles
        scrollbar_section = match.group(3)
        
        return f'''<!-- Common Styles for Teaching Pages -->
    <link rel="stylesheet" href="common-styles.css">

    <style>
        /* Page-specific styles */
        {scrollbar_section}'''
    
    # Apply the replacement
    new_content = re.sub(style_pattern, replace_styles, content, flags=re.DOTALL)
    
    if new_content == content:
        print("⚠️  No style section found to replace")
        return False
    
    # Write back to file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ File updated successfully")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def main():
    """Main function to update all teaching HTML files"""
    base_path = r"g:\My Drive\profile\teaching"
    
    # List of files to update (excluding demo and backup files)
    files_to_update = [
        '720201-B1-1-2568.html',
        '725103-2-2568.html',
        '819605-2-2568.html'
    ]
    
    print("\n" + "="*60)
    print("HTML to Common CSS Converter")
    print("="*60)
    print(f"\nBase path: {base_path}")
    print(f"Files to process: {len(files_to_update)}\n")
    
    success_count = 0
    for filename in files_to_update:
        file_path = os.path.join(base_path, filename)
        if os.path.exists(file_path):
            if update_html_file(file_path):
                success_count += 1
        else:
            print(f"❌ File not found: {filename}")
    
    print("\n" + "="*60)
    print(f"✅ Successfully updated: {success_count}/{len(files_to_update)} files")
    print("="*60)

if __name__ == '__main__':
    main()
