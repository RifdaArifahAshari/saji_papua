# -*- coding: utf-8 -*-
"""
Backend data for Quiz Game.
Contains levels 1-5, each with 5 multiple-choice questions based on Papua suku culture.
"""

# Level 1-5 Questions
QUIZ_DATA = {
    1: [
        {
            "question": "Rumah adat suku Asmat yang juga dikenal sebagai Rumah Bujang adalah...",
            "options": ["Rumah Tsyem", "Rumah Jew", "Rumah Honai", "Rumah Rumsram"],
            "answer": "Rumah Jew"
        },
        {
            "question": "Suku di Papua yang terkenal dengan tradisi potong jari (Iki Palek) sebagai tanda duka cita adalah...",
            "options": ["Suku Asmat", "Suku Dani", "Suku Amungme", "Suku Biak"],
            "answer": "Suku Dani"
        },
        {
            "question": "Puncak Jaya atau Cartensz Pyramid merupakan wilayah adat tempat bermukimnya suku...",
            "options": ["Suku Sentani", "Suku Kamoro", "Suku Amungme", "Suku Asmat"],
            "answer": "Suku Amungme"
        },
        {
            "question": "Alat musik tradisional dari bambu milik suku Dani yang saat ditiup menghasilkan suara mirip kicauan burung adalah...",
            "options": ["Tifa", "Krombi", "Pikon", "Fuu"],
            "answer": "Pikon"
        },
        {
            "question": "Secara umum, tarian adat Papua yang digunakan untuk menyambut tamu penting atau sebagai ungkapan syukur sering diringi dengan alat musik...",
            "options": ["Gamelan", "Angklung", "Tifa", "Sasando"],
            "answer": "Tifa"
        }
    ],
    2: [
        {
            "question": "Pakaian tradisional laki-laki suku Dani yang terbuat dari buah labu air yang dikeringkan disebut...",
            "options": ["Kawat penis", "Koteka", "Sali", "Rok rumbai"],
            "answer": "Koteka"
        },
        {
            "question": "Tari tradisional yang berasal dari suku Asmat, sering digunakan untuk membangkitkan semangat (Tari Perang) adalah...",
            "options": ["Tari Tobe", "Tari Yospan", "Tari Seka", "Tari Sajojo"],
            "answer": "Tari Tobe"
        },
        {
            "question": "Suku Kamoro memiliki tradisi mengukir patung yang mirip dengan Asmat. Rumah adat mereka yang digunakan untuk inisiasi pemuda disebut...",
            "options": ["Rumah Jew", "Karapao", "Honai", "Rumsram"],
            "answer": "Karapao"
        },
        {
            "question": "Suku Biak terkenal sebagai pelaut ulung. Rumah adat suku Biak dinamakan...",
            "options": ["Rumsram", "Ebe'ai", "Tsyem", "Wamai"],
            "answer": "Rumsram"
        },
        {
            "question": "Pakaian laki-laki suku Asmat yang berfungsi sebagai penutup kemaluan sering disebut...",
            "options": ["Yokal", "Sali", "Kawat penis", "Cidako"],
            "answer": "Kawat penis"
        }
    ],
    3: [
        {
            "question": "Pakaian perempuan suku Dani yang BELUM menikah, terbuat dari anyaman rumput atau serat kulit kayu disebut...",
            "options": ["Sali", "Yokal", "Koteka", "Rok rumbai"],
            "answer": "Sali"
        },
        {
            "question": "Tradisi memasak makanan bersama menggunakan batu yang dibakar, terkenal di wilayah Pegunungan Tengah (Suku Dani) disebut...",
            "options": ["Ararem", "Barapen (Bakar Batu)", "Upacara Ndar", "Tindik hidung"],
            "answer": "Barapen (Bakar Batu)"
        },
        {
            "question": "Tari Seka adalah tarian ungkapan rasa syukur masyarakat pesisir selatan Papua. Tarian ini khas dari suku...",
            "options": ["Suku Kamoro", "Suku Biak", "Suku Sentani", "Suku Asmat"],
            "answer": "Suku Kamoro"
        },
        {
            "question": "Suku Sentani banyak mendiami daerah danau. Festival tahunan yang diselenggarakan untuk menampilkan budaya mereka adalah...",
            "options": ["Festival Lembah Baliem", "Festival Danau Sentani", "Festival Asmat", "Festival Biak Munara Wampasi"],
            "answer": "Festival Danau Sentani"
        },
        {
            "question": "Alat musik Krombi terbuat dari bambu dan merupakan alat musik petik/ketuk. Alat musik ini sering dijumpai pada suku...",
            "options": ["Suku Dani", "Suku Asmat", "Suku Tehit", "Suku Amungme"],
            "answer": "Suku Tehit"
        }
    ],
    4: [
        {
            "question": "Pakaian perempuan yang SUDAH menikah pada masyarakat suku Dani, terbuat dari kulit kayu, disebut...",
            "options": ["Sali", "Yokal", "Sali dan Yokal", "Noken"],
            "answer": "Yokal"
        },
        {
            "question": "Ukiran Asmat (seperti Mbitoro atau patung leluhur) sangat terkenal. Tiga warna dominan yang selalu ada dalam ukiran Asmat adalah...",
            "options": ["Merah, Kuning, Hijau", "Merah, Hitam, Putih", "Hitam, Putih, Coklat", "Merah, Hitam, Biru"],
            "answer": "Merah, Hitam, Putih"
        },
        {
            "question": "Pada suku Dani, selain Honai (rumah laki-laki) dan Ebe'ai (rumah perempuan), ada juga rumah khusus babi yang disebut...",
            "options": ["Wamai", "Pilamo", "Karapao", "Jew"],
            "answer": "Wamai"
        },
        {
            "question": "Tari Yosim Pancar (Yospan) merupakan tarian pergaulan yang populer di Papua, hasil penggabungan dua tarian asal daerah...",
            "options": ["Biak dan Yapen", "Asmat dan Kamoro", "Dani dan Amungme", "Sentani dan Nimboran"],
            "answer": "Biak dan Yapen"
        },
        {
            "question": "Salah satu ciri khas masyarakat pesisir Mimika (Suku Kamoro) adalah pemanfaatan pohon sagu. Kuliner ulat sagu sering menjadi hidangan khas dari batang sagu yang membusuk.",
            "options": ["Benar", "Salah", "Hanya dikonsumsi Suku Dani", "Hanya untuk pakan ternak"],
            "answer": "Benar"
        }
    ],
    5: [
        {
            "question": "Suku Amungme memiliki rumah adat yang bentuknya unik menyesuaikan suhu dingin pegunungan. Rumah adat mereka disebut...",
            "options": ["Rumsram", "Jew", "Honai/Wamai (versi Amungme)", "Karapao"],
            "answer": "Honai/Wamai (versi Amungme)"
        },
        {
            "question": "Benda seni berbentuk tiang ukiran leluhur setinggi beberapa meter khas Suku Kamoro yang memiliki nilai magis tinggi disebut...",
            "options": ["Mbitoro", "Tifa berdarah", "Koteka", "Noken"],
            "answer": "Mbitoro"
        },
        {
            "question": "Masyarakat suku Sentani membuat lukisan atau ukiran yang unik, sering menggunakan motif hewan air. Media tradisional yang digunakan melukis adalah...",
            "options": ["Kulit kayu (Malo/Maru)", "Daun lontar", "Kain tenun", "Batu karang"],
            "answer": "Kulit kayu (Malo/Maru)"
        },
        {
            "question": "Sistem kekerabatan atau pernikahan adat suku Biak melibatkan pembayaran mas kawin berupa barang pecah belah berharga yang disebut...",
            "options": ["Ararem", "Barapen", "Iki Palek", "Siri Pinang"],
            "answer": "Ararem"
        },
        {
            "question": "Noken telah diakui oleh UNESCO sebagai warisan budaya tak benda. Fungsi utama Noken bagi suku-suku pegunungan (seperti Dani/Amungme) selain membawa barang adalah...",
            "options": ["Hanya sebagai hiasan dinding", "Membawa hasil kebun dan menggendong anak", "Alat berburu", "Alat musik"],
            "answer": "Membawa hasil kebun dan menggendong anak"
        }
    ]
}

def get_questions_for_level(level: int):
    """Returns a list of 5 questions for the specified level."""
    return QUIZ_DATA.get(level, [])
