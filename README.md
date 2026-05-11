# Technical Test Alphalitical

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-green)
![Requests](https://img.shields.io/badge/Requests-HTTP-orange)

### Business Understanding

Project ini menggunakan teknik **web scraping** dengan Python untuk mengambil data artikel berita dari website **Detik News** selama 8 hari terakhir.
Proses scraping dilakukan menggunakan library `requests` untuk mengambil HTML dari website dan `BeautifulSoup` untuk membaca serta mengekstrak data dari struktur HTML tersebut.

### Architecture

![Architectur](image/architectur.png)

### Extracting Data from HTML

- **Extract**  
  Mengambil HTML dari halaman indeks berita Detik dan mengekstrak data seperti judul berita, URL artikel, dan tanggal publish.
- **Transform**  
  Membersihkan dan memvalidasi data hasil scraping sebelum disimpan ke database.
- **Load**  
  Menyimpan data hasil scraping ke database SQLite pada tabel `news_articles`.

### Extracting Data from HTML

Folder `database` digunakan untuk menyimpan proses yang berhubungan dengan query dan tampilan data dari database SQLite.

- `query_data.py`  
  Berisi SQL query untuk mengambil artikel berita yang dipublikasikan dalam 7 hari terakhir dari tabel `news_articles`.

### Handling Scraping Challenges

#### Cara umum website mencegah web scraping

- `Rate Limiting` → Website membatasi terlalu banyak request dari IP yang sama dalam waktu singkat.
- `CAPTCHA` → Digunakan untuk membedakan antara manusia dan bot.
- `IP Blocking` → IP yang dianggap mencurigakan dapat diblokir oleh website.
- `User-Agent Detection` → Request tanpa header browser biasanya akan terdeteksi sebagai bot.
- `Dynamic Content` → Beberapa website menggunakan JavaScript sehingga data tidak langsung muncul saat di-scrape.

#### Cara menghindari pemblokiran saat scraping

- `Menggunakan User-Agent` → Agar request terlihat seperti browser normal.
- `Memberikan delay antar request` → Menghindari terlalu banyak request dalam waktu singkat.
- `Mematuhi robots.txt` → Mengikuti aturan scraping yang ditetapkan website.
- `Menggunakan Selenium atau Playwright` → Digunakan untuk website yang menggunakan JavaScript rendering.
- `Menghindari scraping berlebihan` → Melakukan scraping secara wajar agar tidak terdeteksi sebagai aktivitas mencurigakan.

### Run Program

- `py main.py`
- `python main.py`
