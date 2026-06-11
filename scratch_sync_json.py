import json

# Read the current chatbot_data.json
with open('chatbot_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# The expanded keywords we made earlier
expanded_categories = {
    "rumah_adat": [
        "rumah adat", "rumah", "honai", "jew", "humai", "komea", "rumsram", "khouw", "tsyem", 
        "ebeai", "karapao", "tempat tinggal", "hunian", "bangunan", "bentuk rumah", "arsitektur",
        "rumah tradisional", "kediaman", "rumah suku", "arsitektur tradisional", "rumah papua"
    ],
    "pakaian_laki_laki": [
        "pakaian adat", "baju adat", "pakaian", "baju", "busana", "pakaian laki-laki", 
        "baju laki-laki", "pakaian pria", "koteka", "kawat penis", "kawatka", "sali", 
        "busana pria", "pakaian adat cowok", "aksesoris pria", "hiasan kepala pria",
        "baju tradisional", "kostum", "pakaian suku", "pakaian tradisional", "pakaian papua"
    ],
    "pakaian_perempuan": [
        "pakaian adat", "baju adat", "pakaian", "baju", "busana", "pakaian perempuan", 
        "baju perempuan", "pakaian wanita", "noken", "cawat perempuan", "rok rumbai", 
        "busana wanita", "pakaian adat cewek", "aksesoris wanita", "perhiasan wanita", 
        "rok daun", "rok serat sagu", "tato perempuan", "baju tradisional", "kostum wanita"
    ],
    "makanan": [
        "makanan", "kuliner", "papeda", "sagu", "ubi", "ulat sagu", "ikan bakar", 
        "makanan khas", "hidangan", "santapan", "makanan pokok", "makanan tradisional", 
        "petatas", "sayur keladi", "babi bakar", "kuliner papua", "makanan suku", "camilan"
    ],
    "tarian": [
        "tarian", "tari", "yamate", "gantar", "bis", "perang", "gemabak", "edlagan", 
        "tumbu tanah", "isosolo", "yospan", "war", "emakwe", "mboti", "ehabla", 
        "gerak tari", "tari-tarian", "kesenian tari", "tari adat", "pesta tari",
        "tari tradisional", "joget", "dansa adat"
    ],
    "hari_besar": [
        "hari besar", "upacara", "festival", "bakar batu", "mbitoro", "wamena", "tikim", 
        "mboti", "pesta panen", "festival budaya", "ritual", "tradisi", "perayaan", 
        "festival lembah baliem", "festival asmat", "festival sentani", "upacara adat"
    ],
    "alat_musik": [
        "alat musik", "musik", "tifa", "fu", "pikon", "embra", "okobere", "gong", 
        "instrumen", "bunyi-bunyian", "alat kesenian", "kererut", "kecapi bambu", 
        "mambisan", "kase", "totobuang"
    ]
}

data['CATEGORIES'] = expanded_categories

# For WISATA_DATA, let's sync the 'nama_suku' attribute from chatbot.html into chatbot_data.json if it doesn't exist
suku_names_map = {
    "biak": "Suku Biak",
    "sentani": "Suku Sentani",
    "amungme": "Suku Amungme",
    "dani": "Suku Dani",
    "kamoro": "Suku Kamoro"
}
for w in data['WISATA_DATA']:
    if 'nama_suku' not in w:
        w['nama_suku'] = suku_names_map.get(w['suku'], "")

with open('chatbot_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("chatbot_data.json updated with expanded keywords and missing fields.")
