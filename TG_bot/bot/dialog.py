from telegram import ParseMode, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
from utils import main_keyboard

def dialog_start(update, context) -> str:
    update.message.reply_text(
        'Как вас зовут? (имя + фамилия)',
        reply_markup=ReplyKeyboardRemove()
    )
    return 'name'


def dialog_name(update, context):
    user_name = update.message.text
    if len(user_name.split()) < 2:
        update.message.reply_text('Пожалуйста введите имя и фамилию!')
        return 'name'
    else:
        context.user_data['dialog'] = {'name': user_name}
        reply_keyboard = [['1', '2', '3', '4', '5']]
        update.message.reply_text('Оцените нашего бота от 1 до 5!', 
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        )
        return 'rating'


def dialog_rating(update, context) -> str:
    context.user_data['dialog']['rating'] = int(update.message.text)
    update.message.reply_text('Напишите комментарий, или нажмите /skip чтобы пропустить')
    return 'comment'


def dialog_comment(update, context) -> str:
    context.user_data['dialog']['comment'] = update.message.text
    user_text = format_output(context.user_data['dialog'])
    update.message.reply_text(user_text, reply_markup=main_keyboard(), parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def dialog_skip(update, context) -> str:
    user_text = format_output(context.user_data['dialog'])
    update.message.reply_text(user_text, reply_markup=main_keyboard(), parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def format_output(dialog) -> str:
    user_text = f"""<b>Имя Фамилия</b>: {dialog['name']}
<b>Оценка</b>: {dialog['rating']}
"""
    if 'comment' in dialog:
        user_text += f'<b>Комментарий</b>: {dialog["comment"]}'
    return user_text


def dialog_fail(update, context):
    update.message.reply_text('Ты прислал что-то не то, напряги извилины и повтори! :)')
