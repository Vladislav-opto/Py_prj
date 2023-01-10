from telegram import ReplyKeyboardRemove

def dialog_start(update, context) -> str:
    update.message.reply_text(
        'Привет, как Вас зовут?',
        reply_markup=ReplyKeyboardRemove()
    )
    return 'name'


def dialog_name(update, context):
    