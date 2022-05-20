import telebot
from telebot import types


bot = telebot.TeleBot("5279468538:AAHrsEL4ORg9E0GkLhFS49UeonwT5wDqPfI")

#РАЙОООООООООООООООООН

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global number
    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.from_user.id, "Привет")
        bot.send_message(message.from_user.id, "Я не так давно в Санкт-Петербурге и знаю пока только 12 районов. Но мои мамы скоро добавят остальные остальные 6 :)")
        distr = ["Адмиралтейский", "Василеостровский", "Выборгский", "Калининский",
                 "Кировский", "Красногвардейский", "Московский", "Невский",
                 "Петроградский", "Приморский", "Фрунзенский" ,"Центральный", "Не имеет значение"]
        markup = telebot.types.InlineKeyboardMarkup()
        for i in range(len(distr)):
            markup.add(telebot.types.InlineKeyboardButton(text=distr[i], callback_data=distr[i]))
        bot.send_message(message.from_user.id, text="Выбери район", reply_markup=markup)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Ой!')
    global call.data
    global answer
    answer = ''
    bot.send_message(call.message.chat.id, call.data)

@bot.message_handler(content_types=['text'])
def cost():
    if answer != 0:
        bot.send_message(message.from_user.id, "Привет")
    else:
        bot.send_message(message.from_user.id, "Пока")


#ЦЕНАААААААААААааа








bot.polling(none_stop=True, interval=0)


















#def get_text_messages(message):
#    if message.text == "Привет" or message.text == "привет":
#        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#    elif message.text == "/help":
#        bot.send_message(message.from_user.id, "Напиши привет")
#    else:
#        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

#name = ''
#surname = ''
#age = 0

#@bot.message_handler(content_types=['text'])
#def start(message):
#    if message.text == '/reg':
#        bot.send_message(message.from_user.id, "Как тебя зовут?")
#        bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
#    else:
#        bot.send_message(message.from_user.id, 'Напиши /reg')

#@bot.message_handler(content_types=['text'])
#def get_name(message): #получаем фамилию
#    global name
#    name = message.text
#    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
#    bot.register_next_step_handler(message, get_surname)

#@bot.message_handler(content_types=['text'])
#def get_surname(message):
#    global surname
#    surname = message.text
#    bot.send_message(message.from_user.id,'Сколько тебе лет?')
#    bot.register_next_step_handler(message, get_age)

#@bot.message_handler(content_types=['text'])
#def get_age(message):
#    global age;
#    while age == 0: #проверяем что возраст изменился
#        try:
#             age = int(message.text) #проверяем, что возраст введен корректно
#        except Exception:
#             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
#    bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')

#@bot.message_handler(content_types=['text'])
#def get_age(message):
#    global age;
#    while age == 0: #проверяем что возраст изменился
#        try:
#             age = int(message.text) #проверяем, что возраст введен корректно
#        except Exception:
#             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
#    keyboard = types.InlineKeyboardMarkup() #наша клавиатура
#    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') #кнопка «Да»
#    keyboard.add(key_yes) #добавляем кнопку в клавиатуру
#    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
#    keyboard.add(key_no)
#    question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
#    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)



#@bot.callback_query_handler(func=lambda call: True)
#def callback_worker(call):
#    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
#        bot.send_message(call.message.chat.id, 'Запомню : )');
#    elif call.data == "no":
#        bot.send_message(call.message.chat.id, 'Сучара : )');

#bot.polling(none_stop=True, interval=0)