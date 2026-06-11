# -*- coding: utf-8 -*-
"""
Backend logic for Indonesian to Tobati translator.
Uses FSA (Finite State Automata) and PDA (Pushdown Automata) simulations for validation
and translation mapping.
"""

import re

# Vocabulary Dictionary based on Tobati lexicon
VOCAB_TOBATI = {
    # Pronouns
    "saya": "Nyak",
    "kamu": "Rau",
    "dia": "Nye",
    "kita": "Mewt",
    "mereka": "Dong",
    "itu": "Nye",
    "ini": "Re",
    
    # Nouns
    "rumah": "Rumsram", # or Rum
    "air": "Fuar",
    "ikan": "Ican",
    "perahu": "Wai",
    "hutan": "Wan",
    "api": "For",
    "batu": "Carcw",
    "pohon": "Yom",
    "makanan": "Nggar",
    
    # Verbs
    "makan": "An",
    "minum": "Nung",
    "tidur": "En",
    "pergi": "Rau",
    "pulang": "Wai",
    "melihat": "Onyo",
    "duduk": "Minyo",
    "berjalan": "Rau",
    "membawa": "Nto",
    
    # Adjectives
    "besar": "Beba",
    "kecil": "Man",
    "baik": "Awor",
    "buruk": "Bruk",
    "cepat": "Truf",
    "jauh": "Awok",
    "dekat": "Ram",
    
    # Greetings
    "halo": "Koi",
    "selamat": "Selamat",
    "pagi": "Bwar",
    "siang": "Syor",
    "sore": "Mandos",
    "malam": "Numbur",
    "terima kasih": "Kuru-kuru"
}

# Reverse mapping for Tobati to Indonesian
VOCAB_INDONESIA = {v.lower(): k for k, v in VOCAB_TOBATI.items()}

def clean_text(text):
    return re.sub(r'[^a-zA-Z\\s]', '', text).lower().strip()

def fsa_validate(words):
    """
    Finite State Automata to validate simple Subject-Predicate-Object (S-P-O) structure.
    Returns True if structurally acceptable for Tobati basic grammar.
    (Simplified simulation)
    """
    if not words: return False
    
    # States: q0 (start), q1 (Subject found), q2 (Verb/Predicate found), q3 (Object found)
    state = "q0"
    
    # Very basic tagging
    subjects = ["saya", "kamu", "dia", "kita", "mereka", "itu", "ini"]
    verbs = ["makan", "minum", "tidur", "pergi", "pulang", "melihat", "duduk", "berjalan", "membawa"]
    
    for word in words:
        if state == "q0" and word in subjects:
            state = "q1"
        elif state in ["q0", "q1"] and word in verbs:
            state = "q2"
        elif state == "q2":
            state = "q3" # Object or adverb
            
    # Valid if it reached a verb (q2) or object (q3), or it's a simple greeting.
    if state in ["q2", "q3"]: return True
    if len(words) <= 2: return True # Accept simple phrases
    return False

def pda_translate_indo_to_tobati(sentence):
    """
    Pushdown Automata simulation for translating Indo to Tobati.
    Handles subject + verb + object order mapping.
    Tobati often uses S-O-V or S-V-O depending on construct, we stick to direct mapped S-V-O here for simplicity.
    """
    words = clean_text(sentence).split()
    if not fsa_validate(words):
        pass # We'll still try to translate word by word if FSA fails
        
    stack = []
    translated_words = []
    
    # Push words onto stack (simulation)
    for word in words:
        stack.append(word)
        
    # Pop and translate (FIFO here for word order preservation)
    for word in words:
        # Get translation, or keep original if not found
        trans = VOCAB_TOBATI.get(word, word)
        # Capitalize first letter of translation
        if trans != word:
            trans = trans.capitalize()
        translated_words.append(trans)
        
    result = " ".join(translated_words)
    return result

def pda_translate_tobati_to_indo(sentence):
    """
    Translates Tobati back to Indonesian.
    """
    words = clean_text(sentence).split()
    translated_words = []
    
    for word in words:
        trans = VOCAB_INDONESIA.get(word, word)
        translated_words.append(trans)
        
    return " ".join(translated_words)
