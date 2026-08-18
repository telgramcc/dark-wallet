import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "توکن_رباتت_اینجا"
OWNER_ID = 8873569921
logging.basicConfig(level=logging.INFO)

def main_menu():
    keyboard = [
        [InlineKeyboardButton("💰 کیف پول من", callback_data="wallet")],
        [InlineKeyboardButton("📥 واریز", callback_data="deposit")],
        [InlineKeyboardButton("📤 برداشت", callback_data="withdraw")],
        [InlineKeyboardButton("💸 انتقال", callback_data="transfer")],
        [InlineKeyboardButton("🔄 تبدیل ارز", callback_data="convert")],
        [InlineKeyboardButton("📊 تاریخچه", callback_data="history")],
        [InlineKeyboardButton("📞 پشتیبانی", callback_data="support")],
        [InlineKeyboardButton("📚 راهنما", callback_data="help")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌑 Dark Wallet\nبه ربات کیف پول خوش اومدی!", reply_markup=main_menu())

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(f"✅ {query.data} انتخاب شد!", reply_markup=main_menu())

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(callback_handler))
print("ربات روشن شد...")
app.run_polling()
