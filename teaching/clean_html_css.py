"""
Clean HTML teaching pages - Remove embedded CSS, keep only page-specific styles
"""
import re

def clean_html_file(file_path, page_specific_css=""):
    """Remove embedded CSS and add common-styles.css link"""
    
    print(f"\n{'='*60}")
    print(f"Processing: {file_path}")
    print('='*60)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False
    
    # Check if already has common-styles.css
    if 'common-styles.css' in content:
        print("⚠️  File already references common-styles.css")
    
    # Find the </script> tag for gtag, then find the <style> and </style> tags
    # Pattern: Find from gtag </script> to </style>
    pattern = r"(gtag\('config', 'G-9VT36QFMKJ'\);\s*</script>)\s*(<style>.*?</style>)"
    
    replacement = r"""\1

    <!-- Common Styles for Teaching Pages -->
    <link rel="stylesheet" href="common-styles.css">

    <style>
        /* Page-specific styles only - All common styles in common-styles.css */
""" + page_specific_css + """
    </style>"""
    
    # Apply replacement
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    if new_content == content:
        print("⚠️  No changes made (pattern not found)")
        return False
    
    # Calculate size reduction
    old_size = len(content)
    new_size = len(new_content)
    reduction = old_size - new_size
    reduction_pct = (reduction / old_size) * 100
    
    # Write back
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ File updated successfully")
        print(f"   Size reduction: {reduction:,} bytes ({reduction_pct:.1f}%)")
        print(f"   Old: {old_size:,} bytes → New: {new_size:,} bytes")
        return True
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def main():
    """Main function"""
    base_path = r"g:\My Drive\profile\teaching"
    
    # Define page-specific styles for each file
    files_config = {
        '720201-B1-1-2568.html': """
        /* Compact sidebar layout */
        /* All styles now in common-styles.css */
""",
        '725103-2-2568.html': """
        /* Compact sidebar layout */
        /* All styles now in common-styles.css */
""",
        '819605-2-2568.html': """
        /* Compact sidebar layout */  
        /* All styles now in common-styles.css */
"""
    }
    
    print("\n" + "="*60)
    print("HTML CSS Cleaner - Remove Embedded Styles")
    print("="*60)
    
    success_count = 0
    import os
    
    for filename, page_css in files_config.items():
        file_path = os.path.join(base_path, filename)
        if os.path.exists(file_path):
            if clean_html_file(file_path, page_css):
                success_count += 1
        else:
            print(f"\n❌ File not found: {filename}")
    
    print("\n" + "="*60)
    print(f"✅ Successfully updated: {success_count}/{len(files_config)} files")
    print("="*60)
    print("\n📝 Next steps:")
    print("1. Open each page in browser to verify")
    print("2. Check that sidebar appears on all pages")
    print("3. Test responsive design (resize browser)")
    print("4. Verify all navigation links work")

if __name__ == '__main__':
    main()
