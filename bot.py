from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Токен бота
TOKEN = "8176904085:AAGm9o8oU9X5ypBOKd-YEmPW7-u-JkRGR_A"

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Создание кнопки с ссылкой на сайт
    keyboard = [
        [
            InlineKeyboardButton("Открыть сайт", url="https://telegram-bot-site.onrender.com")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправка сообщения с кнопкой
    await update.message.reply_text(
        "Добро пожаловать! Нажмите на кнопку ниже, чтобы открыть сайт:",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Бот с Web App запущен...")
    app.run_polling()


