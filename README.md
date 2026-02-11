# 🕌 Bot Waktu Solat Selangor 2026

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg?logo=telegram)](https://t.me/YourBotUsername)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Bot Telegram ringkas dan pantas untuk menyemak waktu solat bagi kawasan Negeri Selangor bagi tahun 2026. Data diambil secara rasmi daripada jadual waktu solat Jabatan Mufti Negeri Selangor.

## ✨ Ciri-ciri
- ✅ **Data Tepat 2026**: Merangkumi ketiga-tiga zon di Selangor.
- ✅ **Format 12 Jam**: Paparan waktu solat dengan format AM/PM yang mesra pengguna.
- ✅ **Kalendar Hijri**: Paparan tarikh Hijri 1447H / 1448H.
- ✅ **Menu Interaktif**: Menggunakan *Inline Keyboard* untuk navigasi yang mudah.
- ✅ **Open Source**: Mudah untuk diubahsuai mengikut keperluan negeri lain.

## 📂 Struktur Projek
```text
├── bot.py                # Kod utama bot
├── zon_1.json           # Data waktu solat Zon 1
├── zon_2.json           # Data waktu solat Zon 2
├── zon_3.json           # Data waktu solat Zon 3
├── requirements.txt      # Senarai library Python
├── Procfile              # Konfigurasi untuk hosting (Render/Koyeb)
├── LICENSE               # Lesen MIT
└── README.md             # Dokumentasi projek

```

## 🚀 Cara Pemasangan (Lokal)

1. **Clone Repository**
```bash
git clone [https://github.com/username/bot-solat-selangor.git](https://github.com/username/bot-solat-selangor.git)
cd bot-solat-selangor

```


2. **Cipta Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Untuk Linux/WSL
# venv\Scripts\activate   # Untuk Windows

```


3. **Install Dependencies**
```bash
pip install -r requirements.txt

```


4. **Set Token Bot**
Dapatkan token daripada [@BotFather](https://t.me/BotFather) dan setkan sebagai environment variable:
```bash
export BOT_TOKEN='token_anda_di_sini'

```


5. **Jalankan Bot**
```bash
python3 bot.py

```



## 🌍 Deployment (Cloud Hosting)

### Render / Koyeb

1. Sambungkan repository GitHub anda ke platform pilihan.
2. Tambahkan **Environment Variable**:
* `BOT_TOKEN`: Masukkan Token API Bot Telegram anda.


3. Gunakan arahan berikut untuk *Start Command*:
```bash
python bot.py

```



## 📍 Pembahagian Zon Selangor

* **Zon 1**: Hulu Selangor, Gombak, Petaling, Hulu Langat, Sepang.
* **Zon 2**: Sabak Bernam, Kuala Selangor.
* **Zon 3**: Klang, Kuala Langat.

## 📜 Lesen

Projek ini dilesenkan di bawah **MIT License**. Anda bebas untuk menyalin dan mengubahsuai kod ini dengan mengekalkan kredit kepada penulis asal.

## 🤝 Sumbangan

Sumbangan (Contribution) amat dialu-alukan! Jika anda mempunyai cadangan atau menjumpai pepijat (bug), sila buka *Issue* atau hantar *Pull Request*.

---

**Penafian**: Data waktu solat adalah anggaran berdasarkan jadual rasmi 2026. Sila rujuk azan di masjid/surau berdekatan untuk kepastian tepat.

```

---

**Satu lagi soalan: Adakah anda perlukan bantuan untuk membuat fail `.env` jika anda mahu buat kerja-kerja pembangunan (development) di PC sendiri tanpa mendedahkan token?**

```
