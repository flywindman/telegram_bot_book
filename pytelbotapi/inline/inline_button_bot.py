import config
import telebot
from telebot import types
# Создаем экземпляр бота
bot = telebot.TeleBot(config.token)

books_name = ['Автор А. Довольно длинное название книги плюс ещё какие-то слова один', 'Автор Б Название книги два']
books_id = [123, 456]
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
    markup_inline = types.InlineKeyboardMarkup()
    for item in range(len(books_name)):
        item_book = types.InlineKeyboardButton(text = books_name[item], callback_data = books_id[item])
        markup_inline.add(item_book)
    bot.send_message(message.chat.id, 'Список найденных книг:', reply_markup = markup_inline)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    book_bron = types.InlineKeyboardMarkup()
    if call.data == '123':
        otvet = 'Забронировали книгу id = ' + call.data
        book_bron.add(types.InlineKeyboardButton(text = 'Забронировать книгу', callback_data = otvet))
        bot.send_message(call.message.chat.id, 'Подробное описание книги 123', reply_markup=book_bron)
    elif call.data == '456':
        otvet = 'Забронировали книгу id = ' + call.data
        book_bron.add(types.InlineKeyboardButton(text = 'Забронировать книгу', callback_data = otvet))
        bot.send_message(call.message.chat.id, 'Подробное описание книги  456', reply_markup=book_bron)
    else:
        bot.send_message(call.message.chat.id, call.data)

    
# Запускаем бота
bot.polling(none_stop=True, interval=0)
