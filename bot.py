import json
import logging
import os
from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# --- KONFIGURASI TOKEN ---
# Jika run di PC (WSL), ia akan cari Token dalam environment variable. 
# Jika tiada, ia akan guna string kosong (Sila set di Hosting nanti).
TOKEN = os.getenv('BOT_TOKEN', '8574758876:AAHaK9qiXIx3SjyMUW3aa8TmtFcgc-aWjoc')

# Konfigurasi Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)

# Fungsi untuk memformat waktu 24j ke 12j dengan AM/PM yang betul
def format_waktu_pintar(waktu_str, nama_solat):
    try:
        # Pecahkan jam dan minit
        jam, minit = map(int, waktu_str.split(':'))
        
        # Logik menentukan AM/PM bagi data JSON yang ringkas
        # Waktu solat selepas Syuruq (Zohor ke atas) biasanya PM
        if nama_solat in ['zohor', 'asar', 'maghrib', 'isya']:
            if jam < 12:
                jam += 12
        
        # Jika jam tepat 12 (Zohor), ia tetap 12 PM
        # Jika jam tepat 24/0 (Imsak/Subuh), ia tetap AM
        
        waktu_obj = datetime.strptime(f"{jam:02d}:{minit:02d}", "%H:%M")
        return waktu_obj.strftime("%I:%M %p")
    except Exception:
        return waktu_str

# Mapping bulan Hijri 2026
def dapatkan_nama_bulan_hijri(tarikh_str):
    bulan = tarikh_str.split('-')[1]
    mapping = {
        "01": "Rejab", "02": "Syaaban", "03": "Ramadhan", "04": "Syawal",
        "05": "Zulkaedah", "06": "Zulhijjah", "07": "Muharram", "08": "Safar",
        "09": "Rabiulawal", "10": "Rabiulakhir", "11": "Jamadilawal", "12": "Jamadilakhir"
    }
    return mapping.get(bulan, "")

# Fungsi membaca data dari JSON
def dapatkan_waktu(zon, tarikh_cari):
    try:
        filename = f'zon_{zon}.json'
        # Gunakan encoding utf-8 untuk mengelakkan isu karakter khas
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for entry in data['jadual']:
            if entry['tarikh'] == tarikh_cari:
                return entry, data['daerah']
    except FileNotFoundError:
        logging.error(f"Fail {filename} tidak dijumpai.")
    except Exception as e:
        logging.error(f"Error: {e}")
    return None, None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Zon 1 (Hulu Selangor, Gombak, Petaling...)", callback_data='1')],
        [InlineKeyboardButton("Zon 2 (Sabak Bernam, Kuala Selangor)", callback_data='2')],
        [InlineKeyboardButton("Zon 3 (Klang, Kuala Langat)", callback_data='3')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_msg = (
        "✨ **Selamat Datang ke Bot Waktu Solat Selangor 2026** ✨\n\n"
        "Sila pilih zon anda untuk mendapatkan waktu solat hari ini:"
    )
    
    if update.message:
        await update.message.reply_text(welcome_msg, reply_markup=reply_markup, parse_mode='Markdown')
    else:
        await update.callback_query.edit_message_text(welcome_msg, reply_markup=reply_markup, parse_mode='Markdown')

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    zon = query.data
    # Tarikh hari ini (format YYYY-MM-DD)
    hari_ini = datetime.now().strftime("%Y-%m-%d")
    
    data_solat, daerah = dapatkan_waktu(zon, hari_ini)

    if data_solat:
        bulan_hijri = dapatkan_nama_bulan_hijri(hari_ini)
        w = data_solat['waktu']
        
        msg = (
            f"🕌 **Waktu Solat Selangor (Zon {zon})**\n"
            f"📍 _{daerah}_\n\n"
            f"📅 **{data_solat['hari']}, {data_solat['tarikh']}**\n"
            f"🌙 **{data_solat['hijri']} {bulan_hijri} 1447H / 1448H**\n\n"
            f"🔹 **Imsak** : {format_waktu_pintar(w['imsak'], 'imsak')}\n"
            f"🔹 **Subuh** : {format_waktu_pintar(w['subuh'], 'subuh')}\n"
            f"🔹 **Syuruq** : {format_waktu_pintar(w['syuruq'], 'syuruq')}\n"
            f"🔹 **Zohor** : {format_waktu_pintar(w['zohor'], 'zohor')}\n"
            f"🔹 **Asar** : {format_waktu_pintar(w['asar'], 'asar')}\n"
            f"🔹 **Maghrib**: {format_waktu_pintar(w['maghrib'], 'maghrib')}\n"
            f"🔹 **Isya'** : {format_waktu_pintar(w['isya'], 'isya')}\n\n"
            "_Sumber: Jabatan Mufti Negeri Selangor_"
        )
        
        keyboard = [[InlineKeyboardButton("⬅️ Kembali ke Menu", callback_data='kembali')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(text=msg, reply_markup=reply_markup, parse_mode='Markdown')
    else:
        await query.edit_message_text(text="❌ Maaf, data waktu solat tidak ditemui.")

if __name__ == '__main__':
    if not TOKEN:
        print("RALAT: Tiada Token dikesan! Sila set BOT_TOKEN.")
    else:
        app = Application.builder().token(TOKEN).build()
        
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(start, pattern='^kembali$'))
        app.add_handler(CallbackQueryHandler(button, pattern='^[1-3]$'))
        
        print("Bot Waktu Solat Selangor sedang berjalan...")
        app.run_polling()
