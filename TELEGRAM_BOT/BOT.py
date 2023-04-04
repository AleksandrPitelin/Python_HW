import telebot
from telebot import types
bot = telebot.TeleBot("5962506375:AAFs4tzAthE_mgeRhCymoenEss128UPl9DQ")

class BotCommands():

    @bot.message_handler(commands=['start'])
    def start(message):
        mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>"
        bot.send_message(message.chat.id, mess, parse_mode="html")

    @bot.message_handler(commands=['youtube'])
    def website(message):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить веб сайт",url="https://www.youtube.com/@user-nd4uj8gt9p"))
        bot.send_message(message.chat.id, "Переходи и подписывайся на мой канал YOUTUBE", reply_markup=markup)

    @bot.message_handler(commands=['help'])
    def website2(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
        website = types.KeyboardButton('/youtube')
        start = types.KeyboardButton('/start')
        markup.add(website,start)
        bot.send_message(message.chat.id, "Переходи на сайт", reply_markup=markup)



@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Вау, крутое фото!")



class Bot_message():
    @bot.message_handler(content_types=['text'])
    def get_user_text(message):
        if message.text =="Hello":
            bot.send_message(message.chat.id, 'И тебе привет!', parse_mode="html")
        elif message.text == "id":
            bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode="html")
        elif message.text == "photo":
            photo = open('/TELEGRAM_BOT/IMG_6399.PNG', 'rb')
            bot.send_photo(message.chat.id, photo)
        else:
            bot.send_message(message.chat.id,"Я тебя не понимаю", parse_mode="html")




bot.polling(none_stop=True)