# -*- coding: utf-8 -*-
"""
Backend logic for Indonesian to Tobati translator.
Uses FSA (Finite State Automata) and PDA (Pushdown Automata) simulations for validation
and translation mapping, specifically designed for SOV/OSV patterns.
"""

import re

# Lexicon & Grammar Rules (Mirrors penerjemah.html)
LEXICON = {
    "subjects": {
        "aka": {"id": "S", "indo": "Saya", "type": "Subjek"},
        "iri": {"id": "S", "indo": "Kamu", "type": "Subjek"},
        "ado": {"id": "S", "indo": "Dia", "type": "Subjek"}
    },
    "objects": {
        "kai": {"id": "O", "indo": "ikan", "type": "Objek"},
        "ham": {"id": "O", "indo": "sagu", "type": "Objek"},
        "te":  {"id": "O", "indo": "air", "type": "Objek"}
    },
    "verbs": {
        "aibi":      {"id": "V", "indo": "menangkap", "type": "Verba"},
        "apri":      {"id": "V", "indo": "makan", "type": "Verba"},
        "ane":       {"id": "V", "indo": "minum", "type": "Verba"},
        "natnahat":  {"id": "V", "indo": "mengajar", "type": "Verba"}
    }
}

PRESETS_VALID = {
    "aka kai aibi": "Saya menangkap ikan",
    "kai aka aibi": "Ikan saya menangkap (Objek dimedepankan)",
    "iri ham apri": "Kamu makan sagu",
    "ado te ane": "Dia minum air"
}

PRESETS_INVALID = {
    "aka aibi kai": "Pola salah (SVO tidak didukung)",
    "ham apri": "Kehilangan Subjek",
    "aka kai": "Kehilangan Verba",
    "iri kai ane": "Terdapat kata lebih / urutan salah"
}

def get_word_info(token):
    if token in LEXICON["subjects"]:
        return LEXICON["subjects"][token]
    elif token in LEXICON["objects"]:
        return LEXICON["objects"][token]
    elif token in LEXICON["verbs"]:
        return LEXICON["verbs"][token]
    return None

def validate_and_translate(sentence):
    """
    Simulates the FSA and PDA logic from penerjemah.html.
    Returns: (is_valid, steps, translation_text, error_msg)
    """
    raw_text = sentence.strip().lower()
    if not raw_text:
        return False, [], "", "Kalimat kosong!"
        
    tokens = raw_text.split()
    
    current_state = "q0"
    stack = ["Z0"]
    
    subjekWord = ""
    objekWord = ""
    verbaWord = ""
    isGrammarValid = True
    
    steps = []
    
    for i, token in enumerate(tokens):
        word_info = get_word_info(token)
        
        step_data = {
            "step": i + 1,
            "token": token,
            "type": "Tidak dikenali",
            "prev_state": current_state,
            "curr_state": current_state,
            "stack": list(stack),
            "status": "info",
            "desc": ""
        }
        
        if not word_info:
            step_data["status"] = "error"
            step_data["desc"] = f"Kata '{token}' tidak ada dalam kamus Tobati!"
            step_data["curr_state"] = "q_err"
            steps.append(step_data)
            isGrammarValid = False
            current_state = "q_err"
            continue
            
        tokenType = word_info["id"]
        step_data["type"] = word_info["type"]
        
        if tokenType == "S": subjekWord = token
        elif tokenType == "O": objekWord = token
        elif tokenType == "V": verbaWord = token
        
        # FSA Transition Logic
        previous_state = current_state
        transitionLabel = ""
        
        if isGrammarValid:
            if current_state == "q0":
                if tokenType == "S":
                    current_state = "q1"
                    transitionLabel = "Membaca Subjek di awal kalimat."
                elif tokenType == "O":
                    current_state = "q2"
                    transitionLabel = "Membaca Objek di awal kalimat."
                else:
                    current_state = "q_err"
                    isGrammarValid = False
                    transitionLabel = "Membaca Verba di awal (Pola tidak valid)."
            elif current_state == "q1":
                if tokenType == "O":
                    current_state = "q3"
                    transitionLabel = "Membaca Objek setelah Subjek."
                else:
                    current_state = "q_err"
                    isGrammarValid = False
                    transitionLabel = "Pola salah (Harus Objek setelah Subjek)."
            elif current_state == "q2":
                if tokenType == "S":
                    current_state = "q4"
                    transitionLabel = "Membaca Subjek setelah Objek."
                else:
                    current_state = "q_err"
                    isGrammarValid = False
                    transitionLabel = "Pola salah (Harus Subjek setelah Objek)."
            elif current_state == "q3":
                if tokenType == "V":
                    current_state = "q5"
                    transitionLabel = "Membaca Verba (Pola SOV)."
                else:
                    current_state = "q_err"
                    isGrammarValid = False
                    transitionLabel = "Pola salah (Harus Verba di akhir)."
            elif current_state == "q4":
                if tokenType == "V":
                    current_state = "q5"
                    transitionLabel = "Membaca Verba (Pola OSV)."
                else:
                    current_state = "q_err"
                    isGrammarValid = False
                    transitionLabel = "Pola salah (Harus Verba di akhir)."
            elif current_state == "q5":
                current_state = "q_err"
                isGrammarValid = False
                transitionLabel = "Token berlebih setelah kalimat selesai."
        else:
            current_state = "q_err"
            
        step_data["curr_state"] = current_state
        step_data["desc"] = f"FSA: {transitionLabel} "
        
        if not isGrammarValid:
            step_data["status"] = "error"
            step_data["desc"] += " [PDA Beku]"
        else:
            # PDA Logic
            if tokenType == "S":
                stack.append("S")
                step_data["desc"] += "| PDA: Push 'S' ke Stack."
            elif tokenType == "O":
                stack.append("O")
                step_data["desc"] += "| PDA: Push 'O' ke Stack."
            elif tokenType == "V":
                if current_state == "q5" and previous_state == "q3": # SOV -> Stack has [Z0, S, O]
                    # Simulate Pop
                    if len(stack) > 1 and stack[-1] == "O": stack.pop()
                    if len(stack) > 1 and stack[-1] == "S": stack.pop()
                    step_data["desc"] += "| PDA: Pop 'O' lalu 'S' dari Stack."
                elif current_state == "q5" and previous_state == "q4": # OSV -> Stack has [Z0, O, S]
                    if len(stack) > 1 and stack[-1] == "S": stack.pop()
                    if len(stack) > 1 and stack[-1] == "O": stack.pop()
                    step_data["desc"] += "| PDA: Pop 'S' lalu 'O' dari Stack."
                    
        step_data["stack"] = list(stack)
        steps.append(step_data)
        
    isFinalAccepting = (current_state == "q5")
    isStackClean = (len(stack) == 1 and stack[0] == "Z0")
    
    if isGrammarValid and isFinalAccepting and isStackClean:
        subIndo = LEXICON["subjects"][subjekWord]["indo"]
        objIndo = LEXICON["objects"][objekWord]["indo"]
        verbIndo = LEXICON["verbs"][verbaWord]["indo"]
        pattern = "SOV" if subjekWord == tokens[0] else "OSV"
        
        translation_text = f"Arti: {subIndo} {verbIndo} {objIndo} (Pola: {pattern})"
        return True, steps, translation_text, ""
    else:
        suggestion = "Gunakan pola bahasa Tobati: Subjek-Objek-Verba (SOV) atau Objek-Subjek-Verba (OSV)."
        if len(tokens) < 3:
            suggestion = "Kalimat tidak lengkap. Minimal membutuhkan 3 kata (Subjek, Objek, dan Verba)."
        elif current_state == "q_err" or not isGrammarValid:
            hasS = any(t in LEXICON["subjects"] for t in tokens)
            hasO = any(t in LEXICON["objects"] for t in tokens)
            hasV = any(t in LEXICON["verbs"] for t in tokens)
            
            if not hasS: suggestion = "Kalimat Anda kehilangan Subjek."
            elif not hasO: suggestion = "Kalimat Anda kehilangan Objek."
            elif not hasV: suggestion = "Kalimat Anda kehilangan Verba."
            else: suggestion = "Struktur kata tidak teratur. Pastikan kata kerja berada di akhir kalimat."
            
        return False, steps, "", suggestion
