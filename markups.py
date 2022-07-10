from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton("На главную")

# -----Main Menu-----
btnStocks = KeyboardButton("Цены Активов")
btnWeather = KeyboardButton("Узнать погоду")
MainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnStocks, btnWeather)

# -----Stocks Menu-----
btnCompany = KeyboardButton("Акции Компаний")
btnMoney = KeyboardButton("Традиционные валюты")
btnCrypto = KeyboardButton("Криптовалюты")
StocksMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCompany,
                                                           btnMoney,
                                                           btnCrypto,
                                                           btnMain)

# -----Exchange Menu-----
btnExchange1 = KeyboardButton("NASDAQ")
btnExchange2 = KeyboardButton("")
btnExchange3 = KeyboardButton("")

# -----Stocks Menu Money-----
btnRub = KeyboardButton("")
btnKz = KeyboardButton("")
btnUSD = KeyboardButton("")
btnEUR = KeyboardButton("")
