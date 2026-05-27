import glob
import re

files = glob.glob('BADMUNDA/BadBoy/*.py')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Update imports
    content = re.sub(r'from \.\. import sudos', r'from .. import sudos, sudo_filter', content)
    content = re.sub(r'from BADMUNDA import sudos', r'from BADMUNDA import sudos, sudo_filter', content)
    
    # Update usages
    content = content.replace("filters.user(sudos)", "sudo_filter")
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated sudo references in {filepath}")
