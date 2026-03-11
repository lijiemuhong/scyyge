#!/usr/bin/env python3
"""Fix search to use original website backend search."""
import os
import re

directory = '/Users/lijiemuhong/.openclaw/workspace/scyyge-english'

for filename in os.listdir(directory):
    if not filename.endswith('.html'):
        continue
    
    filepath = os.path.join(directory, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace search form with one that submits to original website
    old_form = r'<form[^>]*>.*?</form>\s*<div id="searchResults"[^>]*>.*?</div>'
    
    new_form = '''<form action="http://www.scyyge.com/?m=search" method="post" target="_blank">
      <input type="text" name="keyword" value="Search..." onfocus="if(this.value=='Search...') this.value='';" onblur="if(this.value=='') this.value='Search...';" style="width:120px;padding:2px;">
      <button type="submit">Search</button>
    </form>'''
    
    # Use regex to replace
    content = re.sub(
        r'<form[^>]*onsubmit[^>]*>.*?</form>\s*<div[^>]*id="searchResults"[^>]*>.*?</div>',
        new_form,
        content,
        flags=re.DOTALL
    )
    
    # Also try simpler replacement
    if '<form' in content and 'searchInput' in content:
        content = re.sub(
            r'<form[^>]*>.*?<input[^>]*id="searchInput"[^>]*>.*?<button[^>]*>.*?</button>.*?</form>\s*<div[^>]*>.*?</div>',
            new_form,
            content,
            flags=re.DOTALL
        )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed: {filename}")

print("\n✅ Search now uses original website backend!")
print("   - Submits to http://www.scyyge.com/?m=search")
print("   - Opens results in new window")
print("   - Full search functionality from DocCms")
