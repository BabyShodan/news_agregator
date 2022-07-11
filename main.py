import logging
import os

from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils.executor import start_webhook
from aiogram import Bot, types

import markups as nav
from api import *


BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
STOCKS_API_KEY = os.getenv("STOCKS_API")
WEATHER_API_KEY = os.getenv("WEATHER_API")
NEWS_API_KEY = os.getenv("NEWS_API")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/news_agregator/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()


@dp.message_handler(commands=["start"])
async def show_list(message: types.Message) -> None:
    await bot.send_message(message.from_user.id,
                           f"Привет {message.from_user.first_name}!\n"
                           "Я бот-агрегатор новостей! 🤖 \n"
                           "Пожалуйста, выбери функцию из меню",
                           reply_markup=nav.MainMenu)


@dp.message_handler(Text(equals="На главную"))
async def go_back(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, "Вы перемещены в главное меню.", reply_markup=nav.MainMenu)


@dp.message_handler(Text(equals=["Цены активов", "Узнать погоду", "Случайная новость"]))
async def stocks_cos(message: types.Message) -> None:
    """Main menu actions"""
    if message.text == "Цены активов":
        await bot.send_message(message.from_user.id, "Какие активы вас интересуют?", reply_markup=nav.StocksMenu)
    elif message.text == "Узнать погоду":
        await bot.send_message(message.from_user.id, "Выберите интересующий город.", reply_markup=nav.CitiesMenu)
    elif message.text == "Случайная новость":
        await bot.send_message(message.from_user.id, collect_random_news(NEWS_API_KEY))


@dp.message_handler(Text(equals=["Акции компаний", "Традиционные валюты", "Криптовалюты"]))
async def stocks_cos(message: types.Message) -> None:
    if message.text == "Акции компаний":
        await bot.send_message(message.from_user.id,
                               "Выберите интересующую вас акцию из списка",
                               reply_markup=nav.CompanyMenu)
    elif message.text == "Традиционные валюты":
        await bot.send_message(message.from_user.id,
                               "Выберите интересующую вас валюту из списка",
                               reply_markup=nav.MoneyMenu)
    elif message.text == "Криптовалюты":
        await bot.send_message(message.from_user.id,
                               "Выберите интересующую вас криптовалюту из списка",
                               reply_markup=nav.CryptoMenu)
    else:
        await bot.send_message(message.from_user.id,
                               "Я не знаю такой валюты",
                               reply_markup=nav.StocksMenu)


@dp.message_handler(Text(equals=["AAPL", "AAT",
                                 "Рубли", "Тенге", "Доллары", "Евро",
                                 "BTC", "ETH", "Solana", "Near", "Ton", "USDT"]))
async def company_stock(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, collect_stocks_data(STOCKS_API_KEY, message.text))


@dp.message_handler(Text(equals=["Moscow", "Krasnodar"]))
async def weather_info(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, collect_weather_data(WEATHER_API_KEY, message.text))


@dp.message_handler()
async def message_reader(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, "К сожалению я не знаю данной команды 🙁 \n")


print(__name__)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
else:
    raise SystemExit("That's is not a module!")
