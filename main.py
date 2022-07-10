import logging
import os

from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from aiogram import Bot, types

from api import collect_stocks_data, collect_weather_data
import markups as nav


BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
STOCKS_API_KEY = os.getenv("STOCKS_API")
WEATHER_API_KEY = os.getenv("WEATHER_API")
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


@dp.message_handler()
async def message_reader(message: types.Message) -> None:
    if message.text == "Цены активов":
        await bot.send_message(message.from_user.id, "", reply_markup=nav.StocksMenu)
    elif message.text == "Узнать погоду":
        await bot.send_message(message.from_user.id, collect_weather_data())
    else:
        await bot.send_message(message.from_user.id, "К сожалению я не знаю данной команды 🙁 \n"
                                                     "Для справки введите команду: /help")


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
