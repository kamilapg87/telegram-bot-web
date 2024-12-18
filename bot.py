from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Токен вашего бота
TOKEN = "8176904085:AAGm9o8oU9X5ypBOKd-YEmPW7-u-JkRGR_A"

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Кнопка для открытия сайта внутри Telegram
    keyboard = [
        [InlineKeyboardButton("🌐 Открыть сайт", web_app=WebAppInfo(url="https://telegram-bot-site.onrender.com"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Сообщение с кнопкой
    await update.message.reply_text(
        "Нажмите на кнопку ниже, чтобы открыть сайт внутри Telegram:",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    # Создаём и запускаем бота
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Бот с Web App запущен...")
    app.run_polling()
