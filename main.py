import telebot
import buttons as bt


bot = telebot.TeleBot('7471516624:AAEYEfBVEyoDh1NeoJk0gJrGqvtZYtX2o40')


@bot.message_handler(commands=['start'])
def start_message(msg):
    user_id = msg.from_user.id
    bot.send_message(user_id, f'Здравствуйте, {msg.from_user.first_name} 🌺 \n'
                              'Добро пожаловать на нашу кампанию! \n'
                              'Что хотели бы узнать?',
                     reply_markup=bt.main_menu())


@bot.message_handler(content_types=['text'])
def msg(msg):
    user_id = msg.from_user.id
    if msg.text == 'Заказать услугу':
        bot.send_message(user_id, 'Оставьте свой номер телефона',
                         reply_markup=bt.num_button())
    elif msg.text == 'Об услугах':
        bot.send_message(user_id, "Бот еще не доделан, когда додалаю тут появится инфа")
    elif msg.text == 'Цены':
        bot.send_message(user_id, "Бот еще не доделан, когда додалаю тут появится инфа")
    elif msg.text == 'О нас':
        bot.send_message(user_id, "Бот еще не доделан, когда додалаю тут появится инфа")
    elif msg.text == 'Связаться с нами':
        bot.send_message(user_id, "Бот еще не доделан, когда додалаю тут появится инфа")
#    elif msg.text == 'Назад':
#        bot.send_message('Назад в меню', reply_markup=bt.main_menu())


bot.polling(non_stop=True)
