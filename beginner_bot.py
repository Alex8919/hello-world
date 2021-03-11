import telebot

token = '1623822923:AAE6cODVFEP_ERML5S_7Cx3WYCqwn-b3zOc'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
     if message.text == "Привет":
          bot.send_message(message.from_user.id,"Привет, чем я могу тебе помочь?")
     elif message.text == "/help":
          bot.send_message(message.from_user.id, "Напиши привет")
     else:
          bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
     if message.text == "Дата":
          bot.send_message(message.from_user.id, )

          
bot.polling(none_stop=True)
