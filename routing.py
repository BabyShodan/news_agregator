from aiogram import types
from aiogram.dispatcher.filters import Text

from main import dp, bot


@dp.message_handler(commands=["start"])
async def show_list(message: types.Message) -> None:
    await bot.send_message(message.from_user.id,
                           f"Привет {message.from_user.first_name}!\n"
                           "Я бот-агрегатор новостей! 🤖 \n"
                           "Пожалуйста, выбери функцию из меню")


@dp.message_handler()
async def message_reader(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, "К сожалению я не знаю данной команды 🙁 \n"
                                                 "Для справки введите команду: /help")
