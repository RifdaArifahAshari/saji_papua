import re
import json

def parse_galeri():
    with open("galeri.html", "r", encoding="utf-8") as f:
        content = f.read()

    items = []
    # Regex to find onclick="openModal('Cat', 'Title', 'Img', 'Desc')"
    # It might span multiple lines, so we use DOTALL
    pattern = re.compile(r"onclick=\"openModal\(\s*'([^']*)'\s*,\s*'([^']*)'\s*,\s*'([^']*)'\s*,\s*'([^']*)'\s*\)\"", re.DOTALL)
    
    matches = pattern.findall(content)
    
    for match in matches:
        category, title, img, desc = match
        # clean up any excessive whitespace in desc
        desc = re.sub(r'\s+', ' ', desc).strip()
        items.append({
            "category": category,
            "title": title,
            "desc": desc,
            "img": img
        })
        
    # Wait! The data-category attribute is also used for filtering (e.g. 'clothing', 'house').
    # I should also extract the filter category from data-category.
    # Let's use a better regex on the whole div.
    pattern_div = re.compile(r'<div\s+class="gallery-item"\s+data-category="([^"]+)"[\s\S]*?onclick="openModal\(\s*\'([^\']*)\'\s*,\s*\'([^\']*)\'\s*,\s*\'([^\']*)\'\s*,\s*\'([^\']*)\'\s*\)"', re.DOTALL)
    matches_div = pattern_div.findall(content)
    
    better_items = []
    for match in matches_div:
        filter_cat, category, title, img, desc = match
        desc = re.sub(r'\s+', ' ', desc).strip()
        better_items.append({
            "filter_cat": filter_cat,
            "category": category,
            "title": title,
            "desc": desc,
            "img": img
        })

    with open("backend/galeri_data.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nExtracted Gallery Data from galeri.html\n"""\n\n')
        f.write("GALLERY_ITEMS = ")
        f.write(json.dumps(better_items, indent=4, ensure_ascii=False))
        f.write("\n")
        
    print(f"Extracted {len(better_items)} items!")

if __name__ == "__main__":
    parse_galeri()
