import logging
import sys
sys.path.append('../')
import settings
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters, ConversationHandler
from dialog import dialog_start, dialog_name
from handlers import (greet_user, talk_to_me, guess_number, 
                        send_smile, user_coordinates)

logging.basicConfig(filename='bot.log', level=logging.INFO)

def main_function() -> None:
    shopping_manager_bot = Updater(settings.API_KEY, use_context=True)
    dp = shopping_manager_bot.dispatcher

    dialog_structure = ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('^(Заполнить анкету)$'), dialog_start)
        ],
        states={
            'name': [MessaheHandler(Filters.text, dialog_name)]
        },
        fallbacks=[]
    )
    dp.add_handler(dialog_structure)

    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.regex('^(Пришли смайлик!)$'), send_smile))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    shopping_manager_bot.start_polling()
    shopping_manager_bot.idle()

if __name__ == "__main__":
    main_function()
