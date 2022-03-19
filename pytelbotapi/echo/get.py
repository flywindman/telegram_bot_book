import config
import telebot

bot = telebot.TeleBot(config.token)
#upd = bot.get_updates()
#print(upd)
#doc = open('g.txt',  'a')
#doc.write(upd)
#doc.close()

#bot.send_message(1265907833, "Проба")

#upd = bot.get_updates()

#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)


bot.send_message(5146872602, "проверяем, как доходят сообщения из бота к юзеру \nЛюда привет!!!!")
"""
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
     
"""