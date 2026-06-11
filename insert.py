import re

html_file = 'c:\\Kuliah Rifda\\Semester 6\\pelestarian_budaya\\galeri.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

wisata_html = """
                <!-- ===== WISATA ===== -->
                <div class="gallery-item" data-category="tourism"
                    onclick="openModal('Wisata Alam & Budaya','Raja Ampat','assets/images/raja_ampat.jpg','Raja Ampat merupakan destinasi wisata dunia di Papua yang memukau lewat kumpulan pulau besar dan kecil, dengan empat pulau utamanya meliputi Waigeo, Misool, Salawati, dan Batanta. Kawasan ini sangat terkenal dengan kekayaan bawah lautnya yang dihuni oleh penyu laut serta sekitar 1.511 spesies ikan. Bagi para pelancong yang ingin mendapatkan pengalaman menyelam terbaik dengan kondisi cuaca yang mendukung serta visibilitas air laut yang sangat jernih, waktu kunjungan paling ideal adalah pada bulan Oktober dan November.')">
                    <div class="gallery-img-wrapper">
                        <img src="assets/images/raja_ampat.jpg" alt="Raja Ampat">
                    </div>
                    <div class="gallery-card-info">
                        <span class="gallery-item-tag">Wisata</span>
                        <h4>Raja Ampat</h4>
                        <p>Kawasan laut dengan kekayaan bawah laut spektakuler, terkait erat dengan pelaut Biak.</p>
                    </div>
                </div>

                <div class="gallery-item" data-category="tourism"
                    onclick="openModal('Wisata Alam & Budaya','Danau Sentani','assets/images/danau_sentani.jpg','Sebagai danau terbesar di Papua yang terletak di ketinggian 75 meter di atas permukaan laut, Danau Sentani menyuguhkan panorama alam menakjubkan yang dikelilingi oleh sekitar 21 pulau di sekitarnya. Di destinasi ini, para pengunjung dapat menikmati berbagai aktivitas seru seperti berenang, memancing, berkeliling area danau menggunakan perahu yang disewakan, hingga mencicipi kuliner lokal. Selain menikmati keindahan alamnya, kesempatan berinteraksi langsung dengan penduduk setempat juga menjadi salah satu pengalaman berharga yang tidak boleh dilewatkan oleh wisatawan.')">
                    <div class="gallery-img-wrapper">
                        <img src="assets/images/danau_sentani.jpg" alt="Danau Sentani">
                    </div>
                    <div class="gallery-card-info">
                        <span class="gallery-item-tag">Wisata</span>
                        <h4>Danau Sentani</h4>
                        <p>Danau megah tempat tinggal Suku Sentani, terkenal dengan desa terapung dan keindahannya.</p>
                    </div>
                </div>

                <div class="gallery-item" data-category="tourism"
                    onclick="openModal('Wisata Alam & Budaya','Pulau Biak','assets/images/pulau_biak.jpg','Pulau Biak yang berada di Teluk Cenderawasih membentuk Kabupaten Biak bersama Pulau Numfor dan menyimpan ragam destinasi menarik seperti Kampung Amoi di Biak Utara serta Museum Cenderawasih yang mengoleksi peninggalan Perang Dunia II. Wisatawan juga dapat mencicipi kuliner khas Singkong Marapen, mengunjungi Pantai Bosnik dan Air Terjun Wafsarak, atau melihat koleksi flora dan fauna lengkap di Taman Burung dan Taman Anggrek daerah Bosnik.')">
                    <div class="gallery-img-wrapper">
                        <img src="assets/images/pulau_biak.jpg" alt="Pulau Biak">
                    </div>
                    <div class="gallery-card-info">
                        <span class="gallery-item-tag">Wisata</span>
                        <h4>Pulau Biak</h4>
                        <p>Pulau bersejarah dengan pesona pesisir, peninggalan PD II, dan wisata Kampung Amoi.</p>
                    </div>
                </div>

                <div class="gallery-item" data-category="tourism"
                    onclick="openModal('Wisata Alam & Budaya','Taman Nasional Lorentz','assets/images/taman_nasional_lorentz.jpg','Taman Nasional Lorentz merupakan kawasan konservasi terbesar dengan ekosistem terlengkap di Asia Pasifik sekaligus menjadi taman nasional terbesar di Asia Tenggara yang telah diakui sebagai situs warisan dunia oleh UNESCO. Memiliki luas mencapai 2.505.600 hektare yang membentang di 10 kabupaten, taman ini dapat diakses melalui pintu masuk di tiga kota berbeda, yaitu Timika, Wamena, dan Enarotali. Di dalam kawasan megah ini, pengunjung dapat menjumpai berbagai fauna khas Papua yang sangat menarik, seperti puyuh salju, kanguru pohon dingiso, dan cendrawasih ekor panjang.')">
                    <div class="gallery-img-wrapper">
                        <img src="assets/images/taman_nasional_lorentz.jpg" alt="Taman Nasional Lorentz">
                    </div>
                    <div class="gallery-card-info">
                        <span class="gallery-item-tag">Wisata</span>
                        <h4>Taman Nasional Lorentz</h4>
                        <p>Kawasan konservasi alam terbesar di Asia Tenggara, rumah bagi puyuh salju dan dingiso.</p>
                    </div>
                </div>

                <div class="gallery-item" data-category="tourism"
                    onclick="openModal('Wisata Alam & Budaya','Lembah Baliem','assets/images/lembah_baliem.jpg','Terletak di sekitar Pegunungan Jayawijaya, Lembah Baliem menjadi tempat tinggal bagi suku Dani, Yali, dan Lani yang masih mempertahankan gaya hidup tradisional seperti mengenakan koteka dan rok rumbai di tengah peradaban mirip zaman batu yang sebagian besar hanya bisa diakses dengan berjalan kaki atau bersepeda. Setiap bulan Agustus, lembah ini menyelenggarakan Festival Lembah Baliem selama tiga hari yang bertujuan mengurangi konflik antar suku dan berhasil memikat wisatawan melalui atraksi budaya, lomba karapan babi antar desa, serta pesta babi bakar.')">
                    <div class="gallery-img-wrapper">
                        <img src="assets/images/lembah_baliem.jpg" alt="Lembah Baliem">
                    </div>
                    <div class="gallery-card-info">
                        <span class="gallery-item-tag">Wisata</span>
                        <h4>Lembah Baliem</h4>
                        <p>Lembah spektakuler tempat Suku Dani mempertahankan tradisi aslinya.</p>
                    </div>
                </div>

                <div class="gallery-item" data-category="tourism"
                    onclick="openModal('Wisata Alam & Budaya','Air Terjun Wafsarak','assets/images/air_terjun_wafsarak.jpg','Air Terjun Wafsarak yang terletak di Biak Utara, Papua Barat, adalah destinasi wisata setinggi 10 meter yang menawarkan keindahan tersembunyi dan suasana alami di tengah hutan sebagai tempat pelarian dari rutinitas harian. Akses menuju lokasi ini tergolong sangat mudah sehingga suara gemericik airnya sudah dapat terdengar dari pinggir jalan, serta memiliki kolam di bawahnya yang berair sangat jernih. Karena kondisinya yang aman dan ideal untuk berenang maupun bermain air bersama anak-anak, tempat ini menjadi rekomendasi liburan yang sangat tepat untuk dikunjungi bersama keluarga.')">
                    <div class="gallery-img-wrapper">
                        <img src="assets/images/air_terjun_wafsarak.jpg" alt="Air Terjun Wafsarak">
                    </div>
                    <div class="gallery-card-info">
                        <span class="gallery-item-tag">Wisata</span>
                        <h4>Air Terjun Wafsarak</h4>
                        <p>Air terjun jernih setinggi 10 meter di Biak Utara, mudah diakses dan cocok untuk keluarga.</p>
                    </div>
                </div>

                <div class="gallery-item" data-category="tourism"
                    onclick="openModal('Wisata Alam & Budaya','Taman Nasional Teluk Cendrawasih','assets/images/teluk_cenderawasih.jpg','Didominasi oleh wilayah perairan, Taman Nasional Teluk Cenderawasih memegang predikat sebagai kawasan konservasi laut terbesar dan terluas di Indonesia yang menjadi surga bagi para pencinta aktivitas menyelam atau diving. Saat menyelam di perairan yang kaya akan flora dan fauna bawah laut ini, penyelam akan disuguhi ratusan jenis moluska dan ikan, serta berkesempatan bertemu langsung dengan kura-kura, penyu, hiu, dan lumba-lumba. Selain menikmati pesona bawah laut, wisatawan juga dapat menjelajahi pulau-pulau sekitar, termasuk Pulau Mioswaar yang memiliki daya tarik unik berupa gua dengan sumber air panas berkandungan belerang.')">
                    <div class="gallery-img-wrapper">
                        <img src="assets/images/teluk_cenderawasih.jpg" alt="Taman Nasional Teluk Cendrawasih">
                    </div>
                    <div class="gallery-card-info">
                        <span class="gallery-item-tag">Wisata</span>
                        <h4>Taman Nasional Teluk Cendrawasih</h4>
                        <p>Konservasi laut terbesar di Indonesia, surga diving bersama hiu paus.</p>
                    </div>
                </div>

                <div class="gallery-item" data-category="tourism"
                    onclick="openModal('Wisata Alam & Budaya','Taman Nasional Wasur','assets/images/wasur.jpg','Terletak di Kabupaten Merauke dengan luas mencapai 413.810 hektare, Taman Nasional Wasur menyuguhkan petualangan menakjubkan bagi para pelancong karena menyimpan hutan sabana terbesar di Indonesia bahkan di Asia. Tempat ini merupakan habitat bagi kekayaan flora dan fauna khas Papua, di mana sebagian besar hewannya merupakan spesies migran yang hidup tersebar di enam ekosistem berbeda. Berkunjung ke taman nasional ini menjadi sebuah keharusan bagi para wisatawan untuk melengkapi pengalaman liburan mereka di Papua, terutama agar bisa melihat langsung fauna unik seperti burung kasuari.')">
                    <div class="gallery-img-wrapper">
                        <img src="assets/images/wasur.jpg" alt="Taman Nasional Wasur">
                    </div>
                    <div class="gallery-card-info">
                        <span class="gallery-item-tag">Wisata</span>
                        <h4>Taman Nasional Wasur</h4>
                        <p>Hutan sabana terbesar di Asia, habitat beragam fauna unik Papua seperti burung kasuari.</p>
                    </div>
                </div>
"""

new_content = re.sub(r'(\s+)</div>(\s*)<!-- Stats Section -->', r'\n\n' + wisata_html + r'\n\1</div>\2<!-- Stats Section -->', content)

if content == new_content:
    print("Warning: regex did not match")
else:
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success")
