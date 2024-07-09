from telebot import types


def main_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    order = types.KeyboardButton('Заказать услугу')
    service = types.KeyboardButton('Об услугах')
    price = types.KeyboardButton('Цены')
    about = types.KeyboardButton('О нас')
    contact = types.KeyboardButton('Связаться с нами')
    kb.row(order)
    kb.add(service, price, about, contact)
    return kb


def num_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Отправить мой номер 📞', request_contact=True)
    but2 = types.KeyboardButton('Назад')
    kb.add(but1)
    kb.row(but2)
    return kb
