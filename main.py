import time

import requests
from bs4 import BeautifulSoup

from telebot import TeleBot
from telebot.types import Message

from configs import TOKEN
from utils import CATEGORIES, get_category
from keyboards import generate_categories

bot = TeleBot(TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def command_start(message: Message):
    user_id = message.from_user.id

    bot.send_message(user_id,
                     f"Assalom Aleykum. O'zingizga juda yoqqan yangiliklarni tanlang !",
                     reply_markup=generate_categories(CATEGORIES))

@bot.message_handler(func=lambda message: message.text in CATEGORIES)
def send_news(message: Message):
    user_id = message.from_user.id
    category_kr = message.text
    category = get_category(category_kr)
    response = requests.get(f'https://kun.uz/{category}')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    box = soup.find('div', id='dle-content')
    news = box.find_all('div', class_='short-story')
    for article in news[:8]:
        title = article.find('h2', class_='sh-tit').get_text()
        description = article.find('div', class_='sh-pen').get_text(strip=True).split('...')[0]
        link = article.find('a')['href']
        image = 'https://kun.uz/' + article.find('img', class_='lazy-loaded')['data-src']

        time.sleep(3)

        bot.send_message(user_id,
                         f"""Nomlanishi: <b>{title}</b>
Ta'rifi: <i>{description}</i>
Link: {link}
{image}""")


bot.polling(none_stop=True)
