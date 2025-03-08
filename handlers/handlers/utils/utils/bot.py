import logging
import os
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from handlers.start import start
from handlers.help import help_command
from handlers.rules import list_rules
from handlers.stats import stats_command
from handlers.callbacks import button_callback
from handlers.messages import handle_message

# Configurações básicas
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levellevel)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    # Obter token do Telegram do ambiente
    telegram_token = os.environ.get("TELEGRAM_TOKEN")
    if not telegram_token:
        logger.error("Telegram token not found in environment variables")
        return

    # Configurar a aplicação
    application = Application.builder().token(telegram_token).build()

    # Adicionar handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("rules", list_rules))
    application.add_handler(CommandHandler("stats", stats_command))
    
    # Callbacks
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Mensagens
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Iniciar a aplicação
    application.run_polling()

if __name__ == "__main__":
    main()