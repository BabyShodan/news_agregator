from aiogram import types

from main import dp, bot
import markups as nav


@dp.message_handler(commands=["start"])
async def show_list(message: types.Message) -> None:
    await bot.send_message(message.from_user.id,
                           f"Привет {message.from_user.first_name}!\n"
                           "Я бот-агрегатор новостей! 🤖 \n"
                           "Пожалуйста, выбери функцию из меню",
                           reply_markup=nav.MainMenu)


@dp.message_handler()
async def message_reader(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, "К сожалению я не знаю данной команды 🙁 \n"
                                                 "Для справки введите команду: /help")
