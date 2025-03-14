import os
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN = "7882951603:AAEcI_ob6XpP1gSM3AqHqUyf3rR1btOoi7c"


app = Application.builder().token(TOKEN).build()

reply_keyboard = [['Аты-жөндер', 'Word құжатын алу'], ['Презентацияны алу']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Боттың мүмкіндіктері:\n"
        "1. 'Аты-жөндер' — студенттердің аты-жөндерін шығарады.\n"
        "2. 'Word құжатын алу' — боттың қалай жасалғаны туралы ақпаратты жібереді.\n"
        "3. 'Презентацияны алу' — жобаны жасаушылар мен процесі туралы презентацияны жібереді.",
        reply_markup=markup
    )

# /help командасы
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = "Боттың мүмкіндіктері:\n"
    help_text += "1. 'Аты-жөндер' — студенттердің аты-жөндерін шығарады.\n"
    help_text += "2. 'Word құжатын алу' — боттың қалай жасалғаны туралы ақпаратты жібереді.\n"
    help_text += "3. 'Презентацияны алу' — жобаны жасаушылар мен процесі туралы презентацияны жібереді.\n"
    await update.message.reply_text(help_text)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == 'Аты-жөндер':
        await update.message.reply_text("Студенттердің аты-жөні:\n1. Балнұр\n")

    elif text == 'Word құжатын алу':
        file_path = 'word_file.docx'
        if os.path.exists(file_path):
            await update.message.reply_document(document=open(file_path, 'rb'))
        else:
            await update.message.reply_text("⚠️ Қате: Word файлы табылмады!")

    elif text == 'Презентацияны алу':
        file_path = 'presentation.pdf'
        if os.path.exists(file_path):
            await update.message.reply_document(document=open(file_path, 'rb'))
        else:
            await update.message.reply_text("⚠️ Қате: Презентация файлы табылмады!")

async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"Сіз жаздыңыз: {user_message}")

def main():
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, button_handler))

    app.run_polling()

if __name__ == "__main__":
    main()
