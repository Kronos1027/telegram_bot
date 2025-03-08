import i18n
from telegram import Update
from telegram.ext import ContextTypes
from utils.translations import set_locale

# Comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    language = update.effective_user.language_code or 'pt'
    set_locale(language)

    await update.message.reply_text(
        i18n.t('help.message', support_contact='@Nerdimportados')
    )