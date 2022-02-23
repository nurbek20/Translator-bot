import telebot
from telebot import types
from googletrans import Translator

token='5146550373:AAE7UKeV0K3yQ5GR_VUsaSOrQm6-csPnz-U'
bot = telebot.TeleBot(token=token)
translator = Translator()
a = translator.translate('milk', dest='ru')
print(a.text)
@bot.message_handler(commands=['lang']) 
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('с русского на английский')
    item2 = types.KeyboardButton('с английского на русский')
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Выберите язык для перевода', reply_markup=markup)
# def send(message):
#     bot.send_message(message.chat.id, 'Я переводчик-бот')
# @bot.message_handler(content_types='text')
# def send_mess(message):
#     if message.text == 1:
#         client_message = translator.translate(message.text, dest='ru').text
#     # if message.text.lower() == client_message:
#         bot.send_message(message.chat.id, client_message)

print('БОТ работает...')
bot.infinity_polling()