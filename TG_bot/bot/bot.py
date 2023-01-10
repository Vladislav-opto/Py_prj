from emoji import emojize
import logging, sys
sys.path.append('../')
import settings
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
from random import choice, randint

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context) -> None:
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f'Привет! Я помогу тебе с покупками! {context.user_data["emoji"]}')


def get_smile(user_data) -> str:
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, language='alias')
    return user_data['emoji']


def talk_to_me(update, context) -> None:
    text = update.message.text
    update.message.reply_text(text)


def play_random_numbers(user_number: int) -> str:
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Ваше число {user_number}, мое {bot_number}, Вы выиграли!'
    elif user_number == bot_number:
        message = f'Ваше число {user_number}, мое {bot_number}, Ничья!'
    else:
        message = f'Ваше число {user_number}, мое {bot_number}, Вы проиграли!'
    return message


def guess_number(update, context) -> None:
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число!'
    else:
        message = 'Введите целое число!'
    update.message.reply_text(message)


def main_function() -> None:
    shopping_manager_bot = Updater(settings.API_KEY, use_context=True)
    dp = shopping_manager_bot.dispatcher
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    shopping_manager_bot.start_polling()
    shopping_manager_bot.idle()

if __name__ == "__main__":
    main_function()
