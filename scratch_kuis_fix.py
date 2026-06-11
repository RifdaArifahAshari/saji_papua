import re
import json

def parse_kuis():
    with open("kuis.html", "r", encoding="utf-8") as f:
        content = f.read()
        
    match = re.search(r'const QUESTIONS = (\{[\s\S]*?\n        \});', content)
    if not match:
        print("Failed to find QUESTIONS in kuis.html")
        return
        
    js_object = match.group(1)
    
    # Put quotes around integer keys
    js_object = re.sub(r'^\s*(\d+):', r'    "\1":', js_object, flags=re.MULTILINE)
    
    try:
        data = json.loads(js_object)
    except Exception as e:
        print("Failed to parse JSON:", e)
        return

    with open("backend/game.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nBackend data for Quiz Game.\nContains levels 1-5, each with 5 multiple-choice questions based on Papua suku culture.\n"""\n\n')
        
        f.write("QUIZ_DATA = ")
        f.write(repr(data).replace("{", "{\n    ").replace("[{", "[\n        {").replace("},", "},\n       ").replace("],", "],\n    "))
        f.write("\n\n")
        
        f.write("""LEVEL_TITLES = {
    1: "Eksplorasi Dasar: Pemula Budaya",
    2: "Penjelajah Madya: Kearifan Lokal",
    3: "Penyelam Tradisi: Jejak Leluhur",
    4: "Pakar Budaya: Rahasia Tersembunyi",
    5: "Sang Maestro: Pelestari Sejati"
}

LEVEL_POINTS = {
    1: 50,
    2: 100,
    3: 150,
    4: 200,
    5: 250
}

def calculate_level_score(level: int, correct_count: int):
    # Base points per correct answer
    base_points = LEVEL_POINTS.get(level, 50) / 5
    return int(correct_count * base_points)

def get_level_questions(level: int):
    \"\"\"Returns a list of 5 questions for the specified level.\"\"\"
    return QUIZ_DATA.get(str(level), QUIZ_DATA.get(level, []))
""")

    print("Success fixing backend/game.py!")

if __name__ == "__main__":
    parse_kuis()
