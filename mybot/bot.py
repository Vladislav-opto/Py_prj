import logging
from telegram.ext import Updater, CommandHandler #Импортировали Updater из модуля ext библиотеки Telegram.
                                 #Этот модуль отвечает за коммуникацию с сервером Telegram - именно он получает/передает сообщения.
def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater("", use_context=True) #не забудь добавить пароль!!!
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

main()