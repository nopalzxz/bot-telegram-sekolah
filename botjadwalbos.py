from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = '8602768603:AAFbf7gu4nPG1DvjFUv6uqj2Aqt17vZhRb4'

# ================= DATA =================
JADWAL_DATA = {
    "senin": (
        "📅 <b>JADWAL SENIN (X-TKJ 1)</b>\n\n"
        "⏰ 07.30-09.30\n📘 Pendidikan Agama\n👩‍🏫 Dra. Siti Asiah\n\n"
        "⏰ 09.30-11.05\n📘 Pendidikan Pancasila\n👩‍🏫 Siti Rochmaida, S.Pd\n\n"
        "⏰ 11.05-12.50\n📘 Seni Budaya\n👩‍🏫 Gebby Imanda, S.Pd\n\n"
        "⏰ 12.50-14.00\n📘 Sejarah Indonesia\n👨‍🏫 Gunawan, S.Pd"
    ),
    "selasa": (
        "📅 <b>JADWAL SELASA (X-TKJ 1)</b>\n\n"
        "⏰ 07.00-09.40\n📘 Bahasa Indonesia\n👩‍🏫 Nani Sri, S.Pd\n\n"
        "⏰ 09.55-11.55\n📘 Projek IPAS\n👨‍🏫 Slamet Nurhadi, S.Kom\n\n"
        "⏰ 12.25-14.25\n📘 Dasar TJKT\n👨‍🏫 Ade Hermawan, M.Kom"
    ),
    "rabu": (
        "📅 <b>JADWAL RABU (X-TKJ 1)</b>\n\n"
        "⏰ 07.00-08.20\n📘 Bahasa Sunda\n👨‍🏫 Nunu Nugraha, S.Pd\n\n"
        "⏰ 08.20-09.40\n📘 BK / Bimbingan Karir\n👩‍🏫 Desi Saraswati, S.Pd\n\n"
        "⏰ 09.55-11.55\n📘 Dasar TJKT\n👨‍🏫 Ade Hermawan, M.Kom\n\n"
        "⏰ 12.25-14.25\n📘 Projek IPAS\n👨‍🏫 Slamet Nurhadi, S.Kom"
    ),
    "kamis": (
        "📅 <b>JADWAL KAMIS (X-TKJ 1)</b>\n\n"
        "⏰ 07.00-09.00\n📘 Dasar TJKT\n👩‍🏫 Enjang Kusumaningsih, ST\n\n"
        "⏰ 09.00-11.55\n📘 Bahasa Inggris\n👨‍🏫 Slamet Riyadi, S.Pd\n\n"
        "⏰ 12.25-15.05\n📘 Matematika\n👩‍🏫 Nining Yuningsih, S.Pd"
    ),
    "jumat": (
        "📅 <b>JADWAL JUMAT (X-TKJ 1)</b>\n\n"
        "⏰ 07.00-09.00\n📘 PJOK\n👨‍🏫 Sandi Ramadhan, S.Pd\n\n"
        "⏰ 09.00-11.15\n📘 Dasar TJKT\n👩‍🏫 Anggun Susila, ST\n\n"
        "⏰ 11.15-14.25\n📘 Informatika\n👨‍🏫 Aulia Nugraha Saputra, S.Pd"
    )
}

# ================= MENU =================
def main_menu():
    keyboard = [
        [InlineKeyboardButton("📅 Jadwal", callback_data="jadwal")],
        [InlineKeyboardButton("📝 Catatan", callback_data="catatan")],
        [InlineKeyboardButton("📊 Info Kelas", callback_data="info")],
        [InlineKeyboardButton("⏰ Pengingat", callback_data="reminder")]
    ]
    return InlineKeyboardMarkup(keyboard)

def hari_menu():
    keyboard = [
        [InlineKeyboardButton("Senin", callback_data="senin"),
         InlineKeyboardButton("Selasa", callback_data="selasa")],
        [InlineKeyboardButton("Rabu", callback_data="rabu"),
         InlineKeyboardButton("Kamis", callback_data="kamis")],
        [InlineKeyboardButton("Jumat", callback_data="jumat")],
        [InlineKeyboardButton("🔙 Kembali", callback_data="menu")]
    ]
    return InlineKeyboardMarkup(keyboard)

def back_menu():
    return InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Menu", callback_data="menu")]])

# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎓 <b>BOT SEKOLAH X-TKJ 1</b>\n\n"
        "Silakan pilih menu di bawah 👇",
        parse_mode='HTML',
        reply_markup=main_menu()
    )

# ================= BUTTON =================
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # MENU UTAMA
    if data == "menu":
        await query.edit_message_text(
            "🏠 <b>MENU UTAMA</b>\nPilih fitur:",
            parse_mode='HTML',
            reply_markup=main_menu()
        )

    # JADWAL
    elif data == "jadwal":
        await query.edit_message_text(
            "📅 <b>PILIH HARI</b>",
            parse_mode='HTML',
            reply_markup=hari_menu()
        )

    elif data in JADWAL_DATA:
        await query.edit_message_text(
            JADWAL_DATA[data],
            parse_mode='HTML',
            reply_markup=back_menu()
        )

    # CATATAN
    elif data == "catatan":
        await query.edit_message_text(
            "📝 Kirim tugas kamu...\nContoh:\nMatematika halaman 10",
            reply_markup=back_menu()
        )
        context.user_data["mode"] = "catatan"

    # INFO
    elif data == "info":
        await query.edit_message_text(
            "📊 <b>INFO KELAS</b>\n"
            "Kelas: X-TKJ 1\n"
            "Wali: (isi sendiri)\n"
            "Jurusan: TJKT",
            parse_mode='HTML',
            reply_markup=back_menu()
        )

    # REMINDER
    elif data == "reminder":
        await query.edit_message_text(
            "⏰ Fitur pengingat aktif!\n(versi sederhana 😁)",
            reply_markup=back_menu()
        )

# ================= HANDLE TEXT =================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("mode") == "catatan":
        user_id = update.message.from_user.id
        catatan_user[user_id] = update.message.text

        await update.message.reply_text("✅ Catatan tersimpan!")
        context.user_data["mode"] = None

# ================= MAIN =================
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🔥 Bot modern siap digunakan!")
    app.run_polling()