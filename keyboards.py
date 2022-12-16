from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def generate_categories(lst: list):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    category_buttons = []

    for category in lst:
        btn = KeyboardButton(text=category)
        category_buttons.append(btn)

    markup.add(*category_buttons)

    return markup
