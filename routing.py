import os

from aiogram import types
from aiogram.dispatcher.filters import Text

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


@dp.message_handler(Text(equals="На главную"))
async def go_back(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, "Вы перемещены в главное меню.", reply_markup=nav.MainMenu)


@dp.message_handler(Text(equals="Цены активов"))
async def stocks_cos(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, "Какие активы вас интересуют?", reply_markup=nav.StocksMenu)
