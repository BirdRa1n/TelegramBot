import telebot

token = '' #token
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['document'])
def document(message):
    extension = message.document.mime_type.replace('application/', '')   
    print(extension) 

bot.polling()
