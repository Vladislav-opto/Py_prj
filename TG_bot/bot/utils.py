from emoji import emojize
from random import choice, randint
from telegram import ReplyKeyboardMarkup, KeyboardButton
import sys
sys.path.append('../')
import settings

def main_keyboard():
    return ReplyKeyboardMarkup([
        [
            'Пришли смайлик!', KeyboardButton('Прислать мои координаты', request_location=True)
        ], 
        [
            'Заполнить анкету'
        ]
    ])


def get_smile(user_data: dict) -> str:
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, language='alias')
    return user_data['emoji']


def play_random_numbers(user_number: int) -> str:
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Ваше число {user_number}, мое {bot_number}, Вы выиграли!'
    elif user_number == bot_number:
        message = f'Ваше число {user_number}, мое {bot_number}, Ничья!'
    else:
        message = f'Ваше число {user_number}, мое {bot_number}, Вы проиграли!'
    return message
