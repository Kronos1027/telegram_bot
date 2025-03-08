import i18n
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.database import get_db_connection
from utils.translations import set_locale

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username
    language = update.effective_user.language_code or 'pt'

    # Registra o usuário no banco de dados
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute('''
            INSERT INTO users (user_id, username, language)
            VALUES (%s, %s, %s)
            ON CONFLICT (user_id) 
            DO UPDATE SET username = %s, language = %s
        ''', (user_id, username, language, username, language))
    conn.commit()
    conn.close()

    # Define o idioma para o usuário
    set_locale(language)

    keyboard = [
        [InlineKeyboardButton(i18n.t('start.enter_button'), callback_data='enter')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        i18n.t('start.welcome'),
        reply_markup=reply_markup
    )