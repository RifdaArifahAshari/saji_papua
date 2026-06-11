# -*- coding: utf-8 -*-
"""
Backend data and query handlers for Saji Papua Chatbot.
Contains 6 suku x 7 categories (42 entries total).
"""

SUKU_DATA = {
    "asmat": {
        "nama": "Suku Asmat",
        "deskripsi": "Suku Asmat dikenal dengan seni ukiran kayu tradisionalnya yang unik dan sangat dihargai di seluruh dunia, serta sistem kemasyarakatan mereka yang kental dengan upacara adat.",
        "kategori": {
            "rumah_adat": "Rumah Jew (rumah panjang panggung, bisa dihuni 10–12 KK, bahan kayu besi & sagu, tahan 15–20 tahun, fungsi utama tempat tinggal & upacara ukir)",
            "pakaian_laki_laki": "Kawat penis (tutup kemaluan dari labu kering), rok rumbai dari serat sagu atau daun sagu, hiasan bulu kasuari & taring babi",
            "pakaian_perempuan": "Rok rumbai pendek dari serat sagu, tubuh dilumuri tanah liat atau minyak kelapa, kalung dari gigi anjing atau kerang",
            "makanan": "Sagu bakar, papeda, ulat sagu panggang (makanan ritual), ikan bakar, bubur sagu dengan kelapa",
            "tarian": "Tari Yamate (tari perang), Tari Gantar (tari gembira), Tari Bis (tari ritual untuk roh leluhur)",
            "hari_besar": "Festival Pisau (upacara ukir kayu), Festival Asmat (Agustus), upacara Mbitoro (inisiasi pria)",
            "alat_musik": "Tifa (drum dari kayu sagu), Fu (suling bambu), Embra (terompet dari keong laut)"
        }
    },
    "dani": {
        "nama": "Suku Dani",
        "deskripsi": "Suku Dani mendiami daerah pegunungan Lembah Baliem yang subur. Mereka terkenal dengan upacara bakar batu yang ikonik dan penggunaan pakaian adat tradisional.",
        "kategori": {
            "rumah_adat": "Honai (pria), Ebeai (wanita), bentuk bulat/kerucut, bahan kayu & jerami, tahan 10–15 tahun, 1 keluarga inti",
            "pakaian_laki_laki": "Koteka (penutup kemaluan dari labu panjang), aksesoris dari bulu cenderawasih, gelang dari kulit kerang",
            "pakaian_perempuan": "Rok rumbai pendek dari serat tanaman atau daun, tubuh dilumuri lemak babi & tanah liat, noken (tas anyaman) di punggung",
            "makanan": "Ubi jalar (petatas) panggang batu, babi bakar, sayur keladi, papeda sagu, ulat sagu",
            "tarian": "Tari Perang (tiruan perang), Tari Gemabak (tari penyambutan), Tari Edlagan (tari gembira)",
            "hari_besar": "Festival Lembah Baliem (Agustus), upacara Wamena (bakar batu massal), upacara Sumpah Babi (perdamaian)",
            "alat_musik": "Pikon (getaran bambu), Tifa kayu, Fu suling bambu, Kererut (alat musik gesek bambu)"
        }
    },
    "amungme": {
        "nama": "Suku Amungme (Amunge)",
        "deskripsi": "Suku Amungme mendiami dataran tinggi dan pegunungan bersalju di Papua Tengah. Mereka memandang tanah dan alam sebagai bagian sakral dari tubuh leluhur mereka.",
        "kategori": {
            "rumah_adat": "Humai (rumah bulat seperti Honai tapi lebih kecil), bahan kayu & alang-alang, 1 KK, tahan 10 tahun, fungsi tempat tinggal & lumbung",
            "pakaian_laki_laki": "Koteka pendek (dari labu atau kayu), topi dari bulu burung, kalung dari tulang hewan",
            "pakaian_perempuan": "Rok daun atau serat, noken tas punggung, penutup dada dari anyaman serat, tubuh dihias tanah liat merah",
            "makanan": "Ubi jalar, sayur pakis, rebung, daging rusa atau babi bakar, bubur sagu, ikan kecil dari sungai",
            "tarian": "Tari Tumbu Tanah (ritual pertanian), Tari Pesta Ubi (syukuran panen)",
            "hari_besar": "Upacara Tikim (inisiasi anak laki-laki), pesta panen ubi (September–Oktober)",
            "alat_musik": "Tifa kayu, Fu suling bambu, Kecapi bambu (petik)"
        }
    },
    "kamoro": {
        "nama": "Suku Kamoro",
        "deskripsi": "Suku Kamoro hidup di sepanjang wilayah pesisir selatan Papua. Kebudayaan mereka sangat dipengaruhi oleh lingkungan sungai, laut, dan hutan bakau.",
        "kategori": {
            "rumah_adat": "Komea (rumah panggung persegi panjang, dihuni 5–6 KK), bahan kayu & atap sagu, tahan 10–15 tahun, fungsi tempat tinggal & upacara",
            "pakaian_laki_laki": "Kawatka (penutup kemaluan dari kayu atau labu), rok serat sagu, hiasan dari cangkang kerang & bulu kasuari",
            "pakaian_perempuan": "Rok pendek serat sagu, tubuh bertato (motif lingkaran & garis), kalung gigi anjing",
            "makanan": "Papeda, sagu bakar, ikan asap, kepiting bakau, udang sungai, umbi-umbian, ulat sagu",
            "tarian": "Tari Emakwe (tari topeng), Tari Mboti (tari gembira pasca panen)",
            "hari_besar": "Upacara Mboti (pesta sagu setiap 5 tahun sekali), Festival Kamoro (setiap tahun)",
            "alat_musik": "Tifa ukir khas Kamoro, Fu suling bambu, Okobere (alat musik tiup dari keong)"
        }
    },
    "biak": {
        "nama": "Suku Biak",
        "deskripsi": "Suku Biak mendiami kepulauan di Teluk Cenderawasih. Mereka dikenal sebagai pelaut tangguh, penjelajah samudera, serta perajin perahu tradisional yang ulung.",
        "kategori": {
            "rumah_adat": "Rumsram (rumah panggung berbentuk perahu terbalik), bahan kayu besi & atap rumbia, tahan 20–30 tahun, dihuni 2–3 keluarga",
            "pakaian_laki_laki": "Sali (kain cawat), topi dari bulu cenderawasih, perisai dari kayu, gelang dan kalung kerang",
            "pakaian_perempuan": "Sali pendek (kain dari kulit kayu atau serat), rok rumbai, mahkota dari bulu & manik-manik",
            "makanan": "Papeda, ikan kuah kuning (ikan tongkol), sagu lempeng (panggang), umbi-umbian, kelapa muda",
            "tarian": "Tari Yospan (perpaduan tari perang & gembira), Tari War (tari perang)",
            "hari_besar": "Festival Pesisir Biak (Juni–Juli), upacara Naik Rumah Baru (Rumsram), pesta laut",
            "alat_musik": "Tifa Biak (bentuk lebih panjang), Suling bambu, Mambisan (alat musik dari bambu dipukul), Gong kayu"
        }
    },
    "sentani": {
        "nama": "Suku Sentani",
        "deskripsi": "Suku Sentani mendiami kawasan sekitar Danau Sentani yang indah. Kehidupan mereka berpusat pada perairan, kerajinan lukis kulit kayu, serta festival budaya tahunan.",
        "kategori": {
            "rumah_adat": "Khouw (rumah panggung di atas danau/daratan), bahan kayu besi & atap ijuk, tahan 20 tahun, dihuni 1 keluarga besar (3–4 KK)",
            "pakaian_laki_laki": "Cawat dari kulit kayu, hiasan kepala dari bulu cenderawasih, kalung manik-manik & kerang, perisai kayu ukir",
            "pakaian_perempuan": "Rok rumbai dari serat sagu atau daun keladi, penutup dada, noken, banyak perhiasan manik-manik warna-warni",
            "makanan": "Ikan bakar dan goreng (khas Danau Sentani), papeda sagu, umbi-umbian, sayur keladi, sagu lempeng",
            "tarian": "Tari Isosolo (tari selamat datang di atas air), Tari Ehabla (tari perang di panggung)",
            "hari_besar": "Festival Danau Sentani (Juni–Juli), lomba perahu hias, upacara adat Mbate (syukuran ikan)",
            "alat_musik": "Tifa kecil, Fu suling bambu, Kase (alat musik tiup dari bambu), Totobuang (gong kecil kayu)"
        }
    }
}

import urllib.parse
import re
import difflib

CATEGORY_REGEXES = {
    "rumah_adat": re.compile(r'\b(rumah(\s*adat)?|rumh|rmh|honai|jew|humai|komea|rumsram|khouw|tsyem|ebeai|karapao|tempat\s*tinggal|hunian|bangunan|arsitektur)\b', re.IGNORECASE),
    "pakaian_laki_laki": re.compile(r'\b(pakaian|pakian|pkaian|baju|bju|busana)(\s*adat)?(\s*(laki(-laki)?|pria|cowok|cowo|cwok))?\b|\b(koteka|kawat\s*penis|kawatka|sali)\b', re.IGNORECASE),
    "pakaian_perempuan": re.compile(r'\b(pakaian|pakian|pkaian|baju|bju|busana)(\s*adat)?(\s*(perempuan|wanita|cewek|cewe|cwek))?\b|\b(noken|rok\s*(rumbai|daun|serat)|tato(\s*perempuan)?)\b', re.IGNORECASE),
    "makanan": re.compile(r'\b(makan(an)?|mkan(an)?|kuliner|hidangan|santapan|papeda|sagu|ubi|petatas|ulat\s*sagu|ikan\s*bakar|keladi|babi\s*bakar)\b', re.IGNORECASE),
    "tarian": re.compile(r'\b(tari(an)?|trian|yamate|gantar|bis|perang|gemabak|edlagan|tumbu\s*tanah|isosolo|yospan|war|emakwe|mboti|ehabla|kesenian\s*tari)\b', re.IGNORECASE),
    "hari_besar": re.compile(r'\b(hari\s*besar|upacara|upcra|festival|fstival|bakar\s*batu|mbitoro|wamena|tikim|mboti|panen|ritual|tradisi|perayaan)\b', re.IGNORECASE),
    "alat_musik": re.compile(r'\b(alat\s*musik|musik|msk|tifa|fu|pikon|embra|okobere|gong|instrumen|bunyi(-bunyian)?|kererut|kecapi|mambisan|kase|totobuang)\b', re.IGNORECASE)
}

SUKU_REGEXES = {
    "asmat": re.compile(r'\b(asmat)\b', re.IGNORECASE),
    "dani": re.compile(r'\b(dani)\b', re.IGNORECASE),
    "amungme": re.compile(r'\b(amungme|amunge)\b', re.IGNORECASE),
    "kamoro": re.compile(r'\b(kamoro)\b', re.IGNORECASE),
    "biak": re.compile(r'\b(biak)\b', re.IGNORECASE),
    "sentani": re.compile(r'\b(sentani)\b', re.IGNORECASE)
}

CATEGORY_NAMES = {
    "rumah_adat": "🏠 Rumah Adat",
    "pakaian_laki_laki": "👦 Pakaian Adat Laki-laki",
    "pakaian_perempuan": "👧 Pakaian Adat Perempuan",
    "makanan": "🍽️ Makanan Khas",
    "tarian": "💃 Tarian Tradisional",
    "hari_besar": "📅 Hari Besar / Upacara",
    "alat_musik": "🎵 Alat Musik"
}

FAQ_DATA = [
    {
        "pattern": re.compile(r'\b(apa saja|daftar|sebutkan)?\s*suku\b.*\bpapua\b', re.IGNORECASE),
        "answer": "Berdasarkan data yang saya punya, suku-suku di Papua meliputi: Suku Asmat, Suku Dani, Suku Amungme, Suku Kamoro, Suku Biak, dan Suku Sentani."
    },
    {
        "pattern": re.compile(r'\bukiran\s*kayu\b', re.IGNORECASE),
        "answer": "Suku di Papua yang paling terkenal dengan ukiran kayunya adalah **Suku Asmat**."
    },
    {
        "pattern": re.compile(r'\b(beda|perbedaan)\b.*\b(honai|jew|rumsram)\b', re.IGNORECASE),
        "answer": "Perbedaannya terletak pada:\n- **Bentuk & Bahan**: Honai (bulat, jerami), Jew (panjang, panggung, kayu), Rumsram (panggung bentuk perahu terbalik, kayu).\n- **Kapasitas**: Honai (1 keluarga inti), Jew (10-12 KK), Rumsram (2-3 keluarga).\n- **Fungsi**: Honai (tempat tinggal), Jew (pusat upacara & ukir), Rumsram (tempat tinggal pemuda)."
    },
    {
        "pattern": re.compile(r'\bsemua\s*suku\b.*\bkoteka\b', re.IGNORECASE),
        "answer": "Tidak semua. Laki-laki Asmat pakai kawat penis (labu kering), Dani dan Amungme pakai koteka, Kamoro pakai kawatka, Biak dan Sentani pakai cawat/sali dari kain/kulit kayu."
    },
    {
        "pattern": re.compile(r'\bmakanan\b.*\bumum\b', re.IGNORECASE),
        "answer": "Makanan khas Papua yang paling umum di semua suku adalah Papeda, sagu bakar, ulat sagu, ikan bakar, dan ubi jalar."
    },
    {
        "pattern": re.compile(r'\bsemua\s*suku\b.*\btari\s*perang\b', re.IGNORECASE),
        "answer": "Hampir semua memiliki, contoh: Tari Yamate (Asmat), Tari Perang (Dani), Tari Ehabla (Sentani), Tari War (Biak)."
    },
    {
        "pattern": re.compile(r'\bfestival\b.*\b(terbesar|papua)\b', re.IGNORECASE),
        "answer": "Nama festival budaya terbesar di Papua dari data tersebut adalah Festival Lembah Baliem (Dani), Festival Asmat, Festival Danau Sentani, dan Festival Pesisir Biak."
    },
    {
        "pattern": re.compile(r'\b(tinggal|rumah|suku)\b.*\b(atas\s*air|danau)\b', re.IGNORECASE),
        "answer": "Ada, yaitu Suku Sentani (rumah Khouw di atas Danau Sentani) dan sebagian suku Kamoro di pesisir."
    },
    {
        "pattern": re.compile(r'\brumah\s*adat\b.*\bperahu\s*terbalik\b', re.IGNORECASE),
        "answer": "Suku yang punya rumah adat berbentuk perahu terbalik adalah **Suku Biak** dengan rumah adat **Rumsram**."
    },
    {
        "pattern": re.compile(r'\b(apa\s*itu\s*noken|suku.*noken|menggunakan\s*noken)\b', re.IGNORECASE),
        "answer": "Noken adalah tas anyaman dari serat atau kulit kayu, yang digunakan oleh perempuan Dani, Amungme, Kamoro, Sentani, dan lainnya."
    },
    {
        "pattern": re.compile(r'\bsuku\b.*\btato\b', re.IGNORECASE),
        "answer": "Suku yang terkenal dengan tato di tubuh perempuannya adalah **Suku Kamoro** (dengan tato motif lingkaran dan garis)."
    },
    {
        "pattern": re.compile(r'\balat\s*musik\b.*\bkeong\b', re.IGNORECASE),
        "answer": "Ya, ada Suku Asmat (menggunakan Embra) dan Suku Kamoro (menggunakan Okobere)."
    },
    {
        "pattern": re.compile(r'\bwisata\b.*\bmudah\s*dijangkau\b', re.IGNORECASE),
        "answer": "Relatif paling mudah dijangkau: Lembah Baliem (Dani) via Wamena, Danau Sentani via Jayapura, Pulau Biak, dan Agats (Asmat) tapi aksesnya lebih terbatas."
    },
    {
        "pattern": re.compile(r'\bperbedaan\b.*\b(pegunungan|pesisir)\b', re.IGNORECASE),
        "answer": "Perbedaan utama antara suku pegunungan (Dani, Amungme) dan pesisir (Asmat, Kamoro, Biak):\n- **Rumah adat**: Honai/Humai vs Jew/Komea/Rumsram\n- **Pakaian**: Koteka vs kawat penis/cawat\n- **Makanan pokok**: Ubi jalar dominan vs sagu dominan\n- Tarian dan budaya lainnya."
    },
    {
        "pattern": re.compile(r'\b(mempertahankan|budaya\s*asli)\b', re.IGNORECASE),
        "answer": "Masih, tapi dengan tingkat yang berbeda-beda; festival dan upacara adat masih rutin digelar."
    }
]

def generate_chatbot_response(query):
    """
    Analyzes user query and returns structured content based on Papua Suku Culture data.
    """
    
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
            if re.search(r'\b' + re.escape(kw) + r'\b', query, re.IGNORECASE):
                suku_nama = SUKU_DATA[w["suku"]]["nama"]
                resp = f"Berikut adalah informasi mengenai wisata **{w['nama'].upper()}**:\n\n"
                resp += f"*{w['deskripsi']}*\n\n"
                resp += f"Kawasan ini sangat berhubungan erat dengan kebudayaan **{suku_nama}**.\n\n"
                wisata_encoded = urllib.parse.quote(w["nama"])
                resp += f"[🖼️ Lihat Gambar Galeri](galeri.html?filter=tourism&open={wisata_encoded})\n"
                return resp

    if re.search(r'\b(wisata|destinasi|tempat\s*menarik|kunjungi)\b', query, re.IGNORECASE):
        resp = "Papua memiliki banyak destinasi wisata yang luar biasa. Berikut adalah beberapa wisata yang ada di database saya:\n"
        for w in WISATA_DATA:
            resp += f"- **{w['nama']}** (Terkait Suku {w['suku'].capitalize()})\n"
        resp += "\nSilakan sebutkan salah satu tempat di atas jika Anda ingin mengetahui informasi lebih detail!"
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
            if re.search(r'\b' + re.escape(kw) + r'\b', query, re.IGNORECASE):
                resp = f"Berikut adalah informasi mengenai alat musik **{am['nama'].upper()}**:\n\n"
                resp += f"*{am['deskripsi']}*\n\n"
                am_encoded = urllib.parse.quote(am["nama"])
                resp += f"[🖼️ Lihat Gambar Galeri](galeri.html?filter=music&open={am_encoded})\n"
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
            
    # 2. Identify which Category is queried using Regex
    matched_cat = []
    for cat_key, pattern in CATEGORY_REGEXES.items():
        if pattern.search(query):
            matched_cat.append(cat_key)
            
    # 3. NLP SIMILARITY FALLBACK (Kemiripan >= 70%)
    if not matched_suku and not matched_cat:
        query_words = query.lower().split()
        
        SUKU_KEYWORDS = {
            "asmat": ["asmat"], "dani": ["dani"], "amungme": ["amungme", "amunge"],
            "kamoro": ["kamoro"], "biak": ["biak"], "sentani": ["sentani"]
        }
        for skey, kws in SUKU_KEYWORDS.items():
            for kw in kws:
                if difflib.get_close_matches(kw, query_words, n=1, cutoff=0.7):
                    matched_suku.append(skey)
                    break
                    
        CATEGORY_KEYWORDS = {
            "rumah_adat": ["rumah", "adat", "honai", "jew", "rumsram"],
            "pakaian_laki_laki": ["pakaian", "baju", "busana", "pria", "laki", "koteka"],
            "pakaian_perempuan": ["pakaian", "baju", "busana", "wanita", "perempuan", "rok", "noken"],
            "makanan": ["makanan", "kuliner", "makan", "papeda"],
            "tarian": ["tarian", "tari"],
            "hari_besar": ["festival", "upacara", "ritual"],
            "alat_musik": ["musik", "alat", "tifa"]
        }
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
            response = f"Berikut adalah info mengenai **{cat_name}** dari berbagai suku di Papua:\n\n"
            for skey, sdata in SUKU_DATA.items():
                response += f"- **{sdata['nama']}**: {sdata['kategori'][cat_key]}\n"
            
            filter_map = {
                "rumah_adat": "house", "pakaian_laki_laki": "clothing", "pakaian_perempuan": "clothing",
                "makanan": "food", "tarian": "dance", "hari_besar": "festival", "alat_musik": "music"
            }
            response += f"\n[Lihat di Galeri Budaya](galeri.html?filter={filter_map[cat_key]})\n"
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
        response += f"### 🌴 {sdata['nama']}\n"
        response += f"*{sdata['deskripsi']}*\n\n"
        
        if matched_cat:
            # Show only the requested categories
            for ckey in set(matched_cat):
                cat_name = CATEGORY_NAMES[ckey]
                response += f"**{cat_name}**:\n{sdata['kategori'][ckey]}\n"
                
                search_term = sdata['nama']
                if sdata['nama'] == "Suku Asmat":
                    if ckey == "pakaian_laki_laki": search_term += " Laki-laki"
                    if ckey == "pakaian_perempuan": search_term += " Perempuan"
                    
                suku_encoded = urllib.parse.quote(search_term)
                response += f"\n[Lihat Gambar di Galeri Budaya](galeri.html?filter={filter_map[ckey]}&open={suku_encoded})\n\n"
            
            return response.strip()

        else:
            # Show all categories summary
            response += "Berikut adalah rangkuman kebudayaan suku ini:\n"
            for ckey, cat_name in CATEGORY_NAMES.items():
                response += f"- **{cat_name}**: {sdata['kategori'][ckey]}\n"
            
            suku_encoded = urllib.parse.quote(sdata['nama'])
            response += f"\n[Lihat Galeri Suku Ini](galeri.html?open={suku_encoded})\n\n"
            
    return response.strip()
