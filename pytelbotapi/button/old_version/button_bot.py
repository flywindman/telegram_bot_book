import config
import telebot
from telebot import types
# Создаем экземпляр бота
bot = telebot.TeleBot(config.token)
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
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
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15)      
        bot.send_message(m.chat.id, 'Привет, выбери подходящий раздел или введи текст для поиска книги',  reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def categoris_and_find(message):
    bot.send_message(message.chat.id, 'А дальше ещё не работает')               #bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


# Запускаем бота
bot.polling(none_stop=True, interval=0)
