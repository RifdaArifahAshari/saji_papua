import re
import json
import ast

def parse_kuis():
    with open("kuis.html", "r", encoding="utf-8") as f:
        content = f.read()
        
    match = re.search(r'const QUESTIONS = (\{[\s\S]*?\n        \});', content)
    if not match:
        return
        
    js_object = match.group(1)
    
    # We can use regex to put quotes around integer keys
    js_object = re.sub(r'^\s*(\d+):', r'    "\1":', js_object, flags=re.MULTILINE)
    
    try:
        data = json.loads(js_object)
    except Exception as e:
        print("Still failed", e)
        return

    with open("backend/game.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nBackend data for Quiz Game.\nContains levels 1-5, each with 5 multiple-choice questions based on Papua suku culture.\n"""\n\n')
        f.write("QUIZ_DATA = ")
        f.write(repr(data).replace("{", "{\n    ").replace("[{", "[\n        {").replace("},", "},\n       ").replace("],", "],\n    "))
        f.write("\n\n")
        f.write("def get_level_questions(level: int):\n")
        f.write('    """Returns a list of 5 questions for the specified level."""\n')
        f.write("    return QUIZ_DATA.get(str(level), QUIZ_DATA.get(level, []))\n")

    print("Success")

if __name__ == "__main__":
    parse_kuis()
