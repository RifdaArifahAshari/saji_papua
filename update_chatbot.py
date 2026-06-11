import json
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
    py_code = """import re
import difflib
import urllib.parse

"""

    # 1. SUKU_DATA
    py_code += "SUKU_DATA = {\n"
    for suku_key, suku_val in SUKU_DATA.items():
        py_code += f"    \"{suku_key}\": {{\n"
        py_code += f"        \"nama\": {repr(suku_val['nama'])},\n"
        py_code += f"        \"deskripsi\": {repr(suku_val['deskripsi'])},\n"
        py_code += "        \"kategori\": {\n"
        for cat_key, cat_val in suku_val['kategori'].items():
            py_code += f"            \"{cat_key}\": {repr(cat_val)},\n"
        py_code += "        }\n"
        py_code += "    },\n"
    py_code += "}\n\n"

    # 2. WISATA_DATA
    py_code += "WISATA_DATA = [\n"
    for w in WISATA_DATA:
        py_code += "    {\n"
        py_code += f"        \"keywords\": {repr(w['keywords'])},\n"
        py_code += f"        \"nama\": {repr(w['nama'])},\n"
        py_code += f"        \"suku\": {repr(w['suku'])},\n"
        py_code += f"        \"deskripsi\": {repr(w['deskripsi'])}\n"
        py_code += "    },\n"
    py_code += "]\n\n"

    # 3. ALAT_MUSIK_DATA
    py_code += "ALAT_MUSIK_DATA = [\n"
    for am in ALAT_MUSIK_DATA:
        py_code += "    {\n"
        py_code += f"        \"keywords\": {repr(am['keywords'])},\n"
        py_code += f"        \"nama\": {repr(am['nama'])},\n"
        py_code += f"        \"deskripsi\": {repr(am['deskripsi'])}\n"
        py_code += "    },\n"
    py_code += "]\n\n"

    # 4. REGEX PATTERNS for SUKU
    py_code += """SUKU_REGEXES = {
    "asmat": re.compile(r'\\b(asmat)\\b', re.IGNORECASE),
    "dani": re.compile(r'\\b(dani|wamena)\\b', re.IGNORECASE),
    "amungme": re.compile(r'\\b(amungme|amunge)\\b', re.IGNORECASE),
    "kamoro": re.compile(r'\\b(kamoro)\\b', re.IGNORECASE),
    "biak": re.compile(r'\\b(biak)\\b', re.IGNORECASE),
    "sentani": re.compile(r'\\b(sentani)\\b', re.IGNORECASE)
}

"""

    # 5. CATEGORY_KEYWORDS
    py_code += "CATEGORY_KEYWORDS = {\n"
    for cat_key, kw_list in CATEGORIES.items():
        py_code += f"    \"{cat_key}\": {repr(kw_list)},\n"
    py_code += "}\n\n"
    
    # 6. CATEGORY NAMES
    py_code += "CATEGORY_NAMES = {\n"
    for cat_key, cat_name in CATEGORY_NAMES.items():
        py_code += f"    \"{cat_key}\": {repr(cat_name)},\n"
    py_code += "}\n\n"

    # 7. FAQ_DATA (SPECIFIC_QA)
    py_code += "FAQ_DATA = [\n"
    for qa in SPECIFIC_QA:
        pattern = qa['pattern']
        if pattern.startswith('/') and pattern.endswith('/i'):
            pattern = pattern[1:-2]
            py_code += f"    {{\"pattern\": re.compile(r{repr(pattern)}, re.IGNORECASE), \"answer\": {repr(qa['answer'])} }},\n"
        elif pattern.startswith('/') and pattern.endswith('/'):
            pattern = pattern[1:-1]
            py_code += f"    {{\"pattern\": re.compile(r{repr(pattern)}), \"answer\": {repr(qa['answer'])} }},\n"
    py_code += "]\n\n"

    # 8. LOGIC CODE
    py_code += """def generate_chatbot_response(query):
    \"\"\"
    Analyzes user query and returns structured content based on Papua Suku Culture data.
    \"\"\"
    
    # 0. Cek Pencarian Wisata Spesifik (8 Destinasi)
    WISATA_DATA = [
        {
            "keywords": ["raja ampat", "pulau raja ampat", "waigeo", "misool", "salawati", "batanta"],
            "nama": "Raja Ampat",
            "suku": "biak", 
            "deskripsi": "Raja Ampat merupakan destinasi wisata dunia di Papua yang memukau lewat kumpulan pulau besar dan kecil, dengan empat pulau utamanya meliputi Waigeo, Misool, Salawati, dan Batanta. Kawasan ini sangat terkenal dengan kekayaan bawah lautnya yang dihuni oleh penyu laut serta sekitar 1.511 spesies ikan. Bagi para pelancong yang ingin mendapatkan pengalaman menyelam terbaik dengan kondisi cuaca yang mendukung serta visibilitas air laut yang sangat jernih, waktu kunjungan paling ideal adalah pada bulan Oktober dan November."
        },
        {
            "keywords": ["danau sentani", "wisata sentani", "danau terbesar"],
            "nama": "Danau Sentani",
            "suku": "sentani", 
            "deskripsi": "Sebagai danau terbesar di Papua yang terletak di ketinggian 75 meter di atas permukaan laut, Danau Sentani menyuguhkan panorama alam menakjubkan yang dikelilingi oleh sekitar 21 pulau di sekitarnya. Di destinasi ini, para pengunjung dapat menikmati berbagai aktivitas seru seperti berenang, memancing, berkeliling area danau menggunakan perahu yang disewakan, hingga mencicipi kuliner lokal. Selain menikmati keindahan alamnya, kesempatan berinteraksi langsung dengan penduduk setempat juga menjadi salah satu pengalaman berharga yang tidak boleh dilewatkan oleh wisatawan."
        },
        {
            "keywords": ["pulau biak", "kampung amoi", "biak utara", "museum cenderawasih"],
            "nama": "Pulau Biak",
            "suku": "biak", 
            "deskripsi": "Pulau Biak yang berada di Teluk Cenderawasih membentuk Kabupaten Biak bersama Pulau Numfor dan menyimpan ragam destinasi menarik seperti Kampung Amoi di Biak Utara serta Museum Cenderawasih yang mengoleksi peninggalan Perang Dunia II. Wisatawan juga dapat mencicipi kuliner khas Singkong Marapen, mengunjungi Pantai Bosnik dan Air Terjun Wafsarak, atau melihat koleksi flora dan fauna lengkap di Taman Burung dan Taman Anggrek daerah Bosnik."
        },
        {
            "keywords": ["taman nasional lorentz", "lorentz", "puyuh salju", "dingiso"],
            "nama": "Taman Nasional Lorentz",
            "suku": "amungme", 
            "deskripsi": "Taman Nasional Lorentz merupakan kawasan konservasi terbesar dengan ekosistem terlengkap di Asia Pasifik sekaligus menjadi taman nasional terbesar di Asia Tenggara yang telah diakui sebagai situs warisan dunia oleh UNESCO. Memiliki luas mencapai 2.505.600 hektare yang membentang di 10 kabupaten, taman ini dapat diakses melalui pintu masuk di tiga kota berbeda, yaitu Timika, Wamena, dan Enarotali. Di dalam kawasan megah ini, pengunjung dapat menjumpai berbagai fauna khas Papua yang sangat menarik, seperti puyuh salju, kanguru pohon dingiso, dan cendrawasih ekor panjang."
        },
        {
            "keywords": ["lembah baliem", "baliem", "pegunungan jayawijaya", "wamena"],
            "nama": "Lembah Baliem",
            "suku": "dani", 
            "deskripsi": "Terletak di sekitar Pegunungan Jayawijaya, Lembah Baliem menjadi tempat tinggal bagi suku Dani, Yali, dan Lani yang masih mempertahankan gaya hidup tradisional seperti mengenakan koteka dan rok rumbai di tengah peradaban mirip zaman batu yang sebagian besar hanya bisa diakses dengan berjalan kaki atau bersepeda. Setiap bulan Agustus, lembah ini menyelenggarakan Festival Lembah Baliem selama tiga hari yang bertujuan mengurangi konflik antar suku dan berhasil memikat wisatawan melalui atraksi budaya, lomba karapan babi antar desa, serta pesta babi bakar."
        },
        {
            "keywords": ["air terjun wafsarak", "wafsarak", "air terjun"],
            "nama": "Air Terjun Wafsarak",
            "suku": "biak", 
            "deskripsi": "Air Terjun Wafsarak yang terletak di Biak Utara, Papua Barat, adalah destinasi wisata setinggi 10 meter yang menawarkan keindahan tersembunyi dan suasana alami di tengah hutan sebagai tempat pelarian dari rutinitas harian. Akses menuju lokasi ini tergolong sangat mudah sehingga suara gemericik airnya sudah dapat terdengar dari pinggir jalan, serta memiliki kolam di bawahnya yang berair sangat jernih. Karena kondisinya yang aman dan ideal untuk berenang maupun bermain air bersama anak-anak, tempat ini menjadi rekomendasi liburan yang sangat tepat untuk dikunjungi bersama keluarga."
        },
        {
            "keywords": ["taman nasional teluk cendrawasih", "teluk cendrawasih", "pulau mioswaar", "hiu paus"],
            "nama": "Taman Nasional Teluk Cendrawasih",
            "suku": "biak", 
            "deskripsi": "Didominasi oleh wilayah perairan, Taman Nasional Teluk Cenderawasih memegang predikat sebagai kawasan konservasi laut terbesar dan terluas di Indonesia yang menjadi surga bagi para pencinta aktivitas menyelam atau diving. Saat menyelam di perairan yang kaya akan flora dan fauna bawah laut ini, penyelam akan disuguhi ratusan jenis moluska dan ikan, serta berkesempatan bertemu langsung dengan kura-kura, penyu, hiu, dan lumba-lumba. Selain menikmati pesona bawah laut, wisatawan juga dapat menjelajahi pulau-pulau sekitar, termasuk Pulau Mioswaar yang memiliki daya tarik unik berupa gua dengan sumber air panas berkandungan belerang."
        },
        {
            "keywords": ["taman nasional wasur", "wasur", "hutan sabana", "merauke"],
            "nama": "Taman Nasional Wasur",
            "suku": "kamoro", 
            "deskripsi": "Terletak di Kabupaten Merauke dengan luas mencapai 413.810 hektare, Taman Nasional Wasur menyuguhkan petualangan menakjubkan bagi para pelancong karena menyimpan hutan sabana terbesar di Indonesia bahkan di Asia. Tempat ini merupakan habitat bagi kekayaan flora dan fauna khas Papua, di mana sebagian besar hewannya merupakan spesies migran yang hidup tersebar di enam ekosistem berbeda. Berkunjung ke taman nasional ini menjadi sebuah keharusan bagi para wisatawan untuk melengkapi pengalaman liburan mereka di Papua, terutama agar bisa melihat langsung fauna unik seperti burung kasuari."
        }
    ]
    
    for w in WISATA_DATA:
        for kw in w["keywords"]:
            if re.search(r'\\b' + re.escape(kw) + r'\\b', query, re.IGNORECASE):
                suku_nama = SUKU_DATA[w["suku"]]["nama"]
                resp = f"Berikut adalah informasi mengenai wisata **{w['nama'].upper()}**:\\n\\n"
                resp += f"*{w['deskripsi']}*\\n\\n"
                resp += f"Kawasan ini sangat berhubungan erat dengan kebudayaan **{suku_nama}**.\\n\\n"
                wisata_encoded = w["nama"] # No need to URL encode for GALERI_BTN
                resp += f"[GALERI_BTN|tourism|{wisata_encoded}]\\n"
                return resp

    if re.search(r'\\b(wisata|destinasi|tempat\\s*menarik|kunjungi)\\b', query, re.IGNORECASE):
        resp = "Papua memiliki banyak destinasi wisata yang luar biasa. Berikut adalah beberapa wisata yang ada di database saya:\\n"
        for w in WISATA_DATA:
            resp += f"- **{w['nama']}** (Terkait Suku {w['suku'].capitalize()})\\n"
        resp += "\\nSilakan sebutkan salah satu tempat di atas jika Anda ingin mengetahui informasi lebih detail!"
        return resp

    # 0.5. Cek Pencarian Alat Musik Spesifik
    ALAT_MUSIK_DATA = [
        {"keywords": ["amyem"], "nama": "Amyem", "deskripsi": "Alat musik tiup sejenis trompet dari kayu putih milik Suku Web di Kabupaten Keerom, biasa mengiringi tarian daerah Papua."},
        {"keywords": ["atowo"], "nama": "Atowo", "deskripsi": "Alat musik tabuh Papua berbentuk bulat panjang, ringan, dan kecil — dimainkan satu tangan menabuh dengan teknik khusus sebagai hiburan rakyat."},
        {"keywords": ["butshake"], "nama": "Butshake", "deskripsi": "Alat musik rattle dari bambu berisi buah kenari asal Muyu, Merauke — digoyang hingga buah kenari saling bertumbuk menghasilkan irama tarian adat."},
        {"keywords": ["fu", "fuu"], "nama": "Fuu", "deskripsi": "Alat musik tiup dari kayu dan bambu khas Suku Asmat Merauke — berfungsi memanggil penduduk dan mengiringi tarian daerah Papua."},
        {"keywords": ["kecapi mulut", "kecapi bambu"], "nama": "Kecapi Mulut", "deskripsi": "Alat musik dari bambu wulu Suku Dani — dijepit di bibir lalu ditiup sambil menarik tali, menghasilkan nada lembut untuk hiburan."},
        {"keywords": ["krombi"], "nama": "Krombi", "deskripsi": "Alat musik pukul Suku Tehit dari Sorong Selatan — dimainkan dengan kayu kecil untuk mengiringi tari-tarian dalam upacara adat."},
        {"keywords": ["pikon"], "nama": "Pikon", "deskripsi": "Alat musik Suku Dani dengan suara khas yang sumbang — digunakan untuk menghibur diri dan mengisi waktu luang setelah bekerja seharian."},
        {"keywords": ["triton", "terompet kerang", "terompet keong"], "nama": "Triton", "deskripsi": "Alat musik tiup dari kerang besar Papua — dahulu sebagai sinyal komunikasi dan panggilan darurat antar warga, kini menjadi hiburan tradisional."},
        {"keywords": ["yi"], "nama": "Yi", "deskripsi": "Alat musik dari kayu dan bambu berbentuk gempal coklat gelap — suaranya sangat unik, kini semakin langka dan sulit ditemukan."}
    ]

    for am in ALAT_MUSIK_DATA:
        for kw in am["keywords"]:
            if re.search(r'\\b' + re.escape(kw) + r'\\b', query, re.IGNORECASE):
                resp = f"Berikut adalah informasi mengenai alat musik **{am['nama'].upper()}**:\\n\\n"
                resp += f"*{am['deskripsi']}*\\n\\n"
                am_encoded = am["nama"]
                resp += f"[GALERI_BTN|music|{am_encoded}]\\n"
                return resp

    # 1. Check FAQ first using Regex
    for faq in FAQ_DATA:
        if faq["pattern"].search(query):
            return faq["answer"]
            
    # 1. Identify which Suku is queried using Regex
    matched_suku = []
    for key, pattern in SUKU_REGEXES.items():
        if pattern.search(query):
            matched_suku.append(key)
            
    # Match Category using exact phrase boundaries (like in HTML)
    matched_cat = []
    CATEGORY_KEYWORDS = {
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

    # Custom disambiguation for pakaian
    query_lower = query.lower()
    has_laki = bool(re.search(r'\\b(laki|pria|cowok)\\b', query_lower))
    has_perempuan = bool(re.search(r'\\b(perempuan|wanita|cewek)\\b', query_lower))

    for cat_key, kw_list in CATEGORY_KEYWORDS.items():
        for kw in kw_list:
            if re.search(r'\\b' + re.escape(kw) + r'\\b', query_lower):
                matched_cat.append(cat_key)
                break

    # If query explicitly specifies gender, filter out the other one
    if has_laki and not has_perempuan and "pakaian_perempuan" in matched_cat:
        matched_cat.remove("pakaian_perempuan")
    if has_perempuan and not has_laki and "pakaian_laki_laki" in matched_cat:
        matched_cat.remove("pakaian_laki_laki")

    # Fallback Similarity
    if not matched_suku and not matched_cat:
        query_words = query_lower.split()
        
        SUKU_KEYWORDS = {
            "asmat": ["asmat"], "dani": ["dani"], "amungme": ["amungme", "amunge"],
            "kamoro": ["kamoro"], "biak": ["biak"], "sentani": ["sentani"]
        }
        for skey, kws in SUKU_KEYWORDS.items():
            for kw in kws:
                if difflib.get_close_matches(kw, query_words, n=1, cutoff=0.7):
                    matched_suku.append(skey)
                    break
                    
        for ckey, kws in CATEGORY_KEYWORDS.items():
            for kw in kws:
                if difflib.get_close_matches(kw, query_words, n=1, cutoff=0.7):
                    matched_cat.append(ckey)
                    break
                
    # If no specific Suku matched, look for category mentions
    if not matched_suku:
        # Check if the user is asking about a general category across all suku
        if matched_cat:
            cat_key = matched_cat[0]
            cat_name = CATEGORY_NAMES[cat_key]
            response = f"Berikut adalah info mengenai **{cat_name}** dari berbagai suku di Papua:\\n\\n"
            for skey, sdata in SUKU_DATA.items():
                response += f"- **{sdata['nama']}**: {sdata['kategori'][cat_key]}\\n"
            
            filter_map = {
                "rumah_adat": "house", "pakaian_laki_laki": "clothing", "pakaian_perempuan": "clothing",
                "makanan": "food", "tarian": "dance", "hari_besar": "festival", "alat_musik": "music"
            }
            resp_filter = filter_map.get(cat_key, "")
            response += f"\\n[GALERI_BTN|{resp_filter}|]\\n"
            return response
            
        # Fallback Trigger if Similarity < 70% and Regex fails
        return "[FALLBACK]"

    # If Suku matches:
    response = ""
    filter_map = {
        "rumah_adat": "house", "pakaian_laki_laki": "clothing", "pakaian_perempuan": "clothing",
        "makanan": "food", "tarian": "dance", "hari_besar": "festival", "alat_musik": "music"
    }

    for skey in matched_suku:
        sdata = SUKU_DATA[skey]
        response += f"### 🌴 {sdata['nama']}\\n"
        response += f"*{sdata['deskripsi']}*\\n\\n"
        
        if matched_cat:
            # Show only the requested categories
            for ckey in set(matched_cat):
                cat_name = CATEGORY_NAMES[ckey]
                response += f"**{cat_name}**:\\n{sdata['kategori'][ckey]}\\n"
                
                search_term = sdata['nama']
                if sdata['nama'] == "Suku Asmat":
                    if ckey == "pakaian_laki_laki": search_term += " Laki-laki"
                    if ckey == "pakaian_perempuan": search_term += " Perempuan"
                    
                response += f"\\n[GALERI_BTN|{filter_map[ckey]}|{search_term}]\\n\\n"
            
            return response.strip()

        else:
            # Show all categories summary
            response += "Berikut adalah rangkuman kebudayaan suku ini:\\n"
            for ckey, cat_name in CATEGORY_NAMES.items():
                response += f"- **{cat_name}**: {sdata['kategori'][ckey]}\\n"
            
            suku_encoded = sdata['nama']
            response += f"\\n[GALERI_BTN||{suku_encoded}]\\n\\n"
            
    return response.strip()
"""

    with open('backend/chatbot.py', 'w', encoding='utf-8') as pyf:
        pyf.write(py_code)

generate_python()
