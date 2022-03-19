import config
import telebot
from telebot import types
# Создаем экземпляр бота
bot = telebot.TeleBot(config.token)

print(bot.get_me())

def log(message, answer):
    print("\n_____________________________________")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1} (id = {2})\nЗапрос: {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))
    print(answer)
    doc_log = open('log.txt',  'a')                      #открываем файл для записи лога
    doc_log.write('\n____________________\n')
    doc_log.write(str(datetime.now())+"\nСообщение от {0} {1} (id = {2})\nЗапрос: {3}\n".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))
    doc_log.write(answer + "\n")
    doc_log.close()             #Закрываем файл

user_dict = {}

class User:
    def __init__(self, name):
        self.name = name
        self.city = None
        self.contact = None


@bot.message_handler(commands=["start"])
def start(message):
        # Добавляем кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("/anketa")
        item2=types.KeyboardButton("что-то еще")
        markup.add(item1, item2)      
        # узнаем имя message.from_user.first_name
        answer='Привет, {0}, пока можно только пройти регистрацию'.format(message.from_user.first_name) 
        bot.send_message(message.chat.id, answer,  reply_markup=markup)
        bot.send_message(1265907833, "Сообщение от {0} {1} (id = {2})\nЗапрос: {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), message.text))
        log(message, answer)
        






# Handle '/anketa'
@bot.message_handler(commands=['anketa'])
def send_welcome(message):
    answer = "Введите ваше Имя Фамилию Отчество"
    msg = bot.reply_to(message, answer)
    log(message, answer)
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, "Укажите адрес для отправки почтой с индексом " )
        bot.register_next_step_handler(msg, process_city_step)
    except Exception as e:
        bot.reply_to(message, 'oooops имя')


def process_city_step(message):
    try:
        chat_id = message.chat.id
        city = message.text
        user = user_dict[chat_id]
        user.city = city
        msg = bot.reply_to(message, "Введите контактные данные для связи (телефон, e-mail, что угодно" )
        bot.register_next_step_handler(msg, process_contact_step)
    except Exception as e:
        bot.reply_to(message, 'oooops город')


def process_contact_step(message):
    try:
        chat_id = message.chat.id
        contact = message.text
        user = user_dict[chat_id]
        user.contact = contact
        answer = 'Ваши даные: \n ' + user.name + '\n Адрес:  ' + str(user.city) + '\n Контакт:  ' + user.contact
        bot.send_message(chat_id, answer)
        bot.send_message(1265907833, "Сообщение от {0} {1} (id = {2})\nАнкета: {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), answer))
        bot.send_message(-618431068, "Сообщение от {0} {1} (id = {2})\nАнкета: {3}".format(message.from_user.first_name, message.from_user.last_name, str(message.from_user.id), answer))
        log(message, answer)
    except Exception as e:
        bot.reply_to(message, 'oooops контакты')


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

# Запускаем бота
bot.polling(none_stop=True, interval=0)
