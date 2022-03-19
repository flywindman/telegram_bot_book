import config
import telebot
from telebot import types
# Создаем экземпляр бота
bot = telebot.TeleBot(config.token)

# сделаем лог файл__________________________________________
print(bot.get_me())
def log(message, answer):
    print("\n_____________________________________")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1} (id = {2})\nЗапрос: {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))
    print(answer)
#_______________________________________________________________

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
        # Добавляем кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        poisk_po_avtoru=types.KeyboardButton("Поиск по автору")
        poisk_po_nazvaniu=types.KeyboardButton("Поиск по названию")
        item1=types.KeyboardButton("Автографы")
        item2=types.KeyboardButton("Детектив")
        item3=types.KeyboardButton("Детская")
        item4=types.KeyboardButton("Иркутские")
        item5=types.KeyboardButton("Искусство")
        item6=types.KeyboardButton("История")
        item7=types.KeyboardButton("Классика")
        item8=types.KeyboardButton("Книги до 1945")
        item9=types.KeyboardButton("Научпоп")
        item10=types.KeyboardButton("Нонфикшн")
        item11=types.KeyboardButton("Поэзия")
        item12=types.KeyboardButton("Проза")
        item13=types.KeyboardButton("Профлит")
        item14=types.KeyboardButton("Роман")
        item15=types.KeyboardButton("Фантастика")        
        markup.add(poisk_po_avtoru, poisk_po_nazvaniu, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15)      
        # узнаем имя message.from_user.first_name
        answer='Привет, {0}, выбери подходящий раздел или введи текст для поиска книги'.format(message.from_user.first_name) 
        bot.send_message(message.chat.id, answer,  reply_markup=markup)
        log(message, answer)
        


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def categoris_and_find(message):
    answer = 'А дальше ещё не работает'
    bot.send_message(message.chat.id, answer)               #bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
    log(message, answer)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
