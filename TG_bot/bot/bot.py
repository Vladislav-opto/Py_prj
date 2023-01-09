import logging, settings
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context) -> None:
    update.message.reply_text('Привет, пользователь! Добро пожаловать ко мне - боту-помощнику с твоими покупками!')


def talk_to_me(update, context) -> None:
    text = update.message.text
    update.message.reply_text(text)


def main_function() -> None:
    shopping_manager_bot = Updater(settings.API_KEY, use_context=True)
    dp = shopping_manager_bot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Бот стартовал!')
    shopping_manager_bot.start_polling()
    shopping_manager_bot.idle()

if __name__ == "__main__":
    main_function()
