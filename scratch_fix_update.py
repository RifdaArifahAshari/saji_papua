import os

# 1. Read the perfect logic from backend/chatbot.py
with open("backend/chatbot.py", "r", encoding="utf-8") as f:
    backend_code = f.read()

# We need to extract the generate_chatbot_response function and everything below it
idx = backend_code.find("def generate_chatbot_response(query):")
logic_code = backend_code[idx:]

# 2. Read the current update_chatbot.py
with open("update_chatbot.py", "r", encoding="utf-8") as f:
    update_code = f.read()

# 3. We will modify update_chatbot.py to use `logic_code` as the string template for the bottom half.
# Notice that `backend/chatbot.py` uses CATEGORY_KEYWORDS which is statically defined in `backend/chatbot.py` currently!
# We want update_chatbot.py to generate CATEGORY_KEYWORDS from CATEGORIES!

new_update_code = """import json
import re

with open('chatbot_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

SUKU_DATA = data['KNOWLEDGE_BASE']
WISATA_DATA = data['WISATA_DATA']
ALAT_MUSIK_DATA = data['ALAT_MUSIK_DATA']
SPECIFIC_QA = data['SPECIFIC_QA']
CATEGORIES = data['CATEGORIES']
CATEGORY_NAMES = data['CATEGORY_NAMES']

def generate_python():
    py_code = \"\"\"import re
import difflib
import urllib.parse

\"\"\"

    # 1. SUKU_DATA
    py_code += "SUKU_DATA = {\\n"
    for suku_key, suku_val in SUKU_DATA.items():
        py_code += f"    \\\"{suku_key}\\\": {{\\n"
        py_code += f"        \\\"nama\\\": {repr(suku_val['nama'])},\\n"
        py_code += f"        \\\"deskripsi\\\": {repr(suku_val['deskripsi'])},\\n"
        py_code += "        \\\"kategori\\\": {\\n"
        for cat_key, cat_val in suku_val['kategori'].items():
            py_code += f"            \\\"{cat_key}\\\": {repr(cat_val)},\\n"
        py_code += "        }\\n"
        py_code += "    },\\n"
    py_code += "}\\n\\n"

    # 2. WISATA_DATA
    py_code += "WISATA_DATA = [\\n"
    for w in WISATA_DATA:
        py_code += "    {\\n"
        py_code += f"        \\\"keywords\\\": {repr(w['keywords'])},\\n"
        py_code += f"        \\\"nama\\\": {repr(w['nama'])},\\n"
        py_code += f"        \\\"suku\\\": {repr(w['suku'])},\\n"
        py_code += f"        \\\"deskripsi\\\": {repr(w['deskripsi'])}\\n"
        py_code += "    },\\n"
    py_code += "]\\n\\n"

    # 3. ALAT_MUSIK_DATA
    py_code += "ALAT_MUSIK_DATA = [\\n"
    for am in ALAT_MUSIK_DATA:
        py_code += "    {\\n"
        py_code += f"        \\\"keywords\\\": {repr(am['keywords'])},\\n"
        py_code += f"        \\\"nama\\\": {repr(am['nama'])},\\n"
        py_code += f"        \\\"deskripsi\\\": {repr(am['deskripsi'])}\\n"
        py_code += "    },\\n"
    py_code += "]\\n\\n"

    # 4. REGEX PATTERNS for SUKU
    py_code += \"\"\"SUKU_REGEXES = {
    "asmat": re.compile(r'\\\\b(asmat)\\\\b', re.IGNORECASE),
    "dani": re.compile(r'\\\\b(dani|wamena)\\\\b', re.IGNORECASE),
    "amungme": re.compile(r'\\\\b(amungme|amunge)\\\\b', re.IGNORECASE),
    "kamoro": re.compile(r'\\\\b(kamoro)\\\\b', re.IGNORECASE),
    "biak": re.compile(r'\\\\b(biak)\\\\b', re.IGNORECASE),
    "sentani": re.compile(r'\\\\b(sentani)\\\\b', re.IGNORECASE)
}

\"\"\"

    # 5. CATEGORY_KEYWORDS
    py_code += "CATEGORY_KEYWORDS = {\\n"
    for cat_key, kw_list in CATEGORIES.items():
        py_code += f"    \\\"{cat_key}\\\": {repr(kw_list)},\\n"
    py_code += "}\\n\\n"
    
    # 6. CATEGORY NAMES
    py_code += "CATEGORY_NAMES = {\\n"
    for cat_key, cat_name in CATEGORY_NAMES.items():
        py_code += f"    \\\"{cat_key}\\\": {repr(cat_name)},\\n"
    py_code += "}\\n\\n"

    # 7. FAQ_DATA (SPECIFIC_QA)
    py_code += "FAQ_DATA = [\\n"
    for qa in SPECIFIC_QA:
        pattern = qa['pattern']
        if pattern.startswith('/') and pattern.endswith('/i'):
            pattern = pattern[1:-2]
            py_code += f"    {{\\\"pattern\\\": re.compile(r{repr(pattern)}, re.IGNORECASE), \\\"answer\\\": {repr(qa['answer'])} }},\\n"
        elif pattern.startswith('/') and pattern.endswith('/'):
            pattern = pattern[1:-1]
            py_code += f"    {{\\\"pattern\\\": re.compile(r{repr(pattern)}), \\\"answer\\\": {repr(qa['answer'])} }},\\n"
    py_code += "]\\n\\n"

    # 8. LOGIC CODE
    py_code += \"\"\"""" + logic_code.replace("\\", "\\\\").replace('"""', '\\"\\"\\"') + """\"\"\"

    with open('backend/chatbot.py', 'w', encoding='utf-8') as pyf:
        pyf.write(py_code)

generate_python()
"""

with open("update_chatbot.py", "w", encoding="utf-8") as f:
    f.write(new_update_code)

print("update_chatbot.py has been successfully rewritten!")
