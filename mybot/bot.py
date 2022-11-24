import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters #Импортировали Updater из модуля ext библиотеки Telegram.
                                 #Этот модуль отвечает за коммуникацию с сервером Telegram - именно он получает/передает сообщения.
import settings
logging.basicConfig(filename="bot.log", level=logging.INFO, encoding='utf-8')

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)
def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
<<<<<<< HEAD
    mybot = Updater(settings.API_KEY, use_context=True)
=======
    mybot = Updater("", use_context=True) #не забудь добавить пароль!!!
>>>>>>> 6cefb098ab325b6318c5958cbcd2b20b67c9dee8
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    # Командуем боту начать ходить в Telegram за сообщениями
    logging.info("Бот стартовал!")
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()
if __name__ == "__main__":
    main()