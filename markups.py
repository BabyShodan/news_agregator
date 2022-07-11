from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton("На главную")

# -----Main Menu-----
btnStocks = KeyboardButton("Цены активов")
btnWeather = KeyboardButton("Узнать погоду")
btnNews = KeyboardButton("Показать новости")
MainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnStocks, btnWeather, btnNews)

# -----Stocks Menu-----
btnCompany = KeyboardButton("Акции компаний")
btnMoney = KeyboardButton("Традиционные валюты")
btnCrypto = KeyboardButton("Криптовалюты")
StocksMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCompany,
                                                           btnMoney,
                                                           btnCrypto,
                                                           btnMain,)


# -----Stocks Menu Money-----
btnRub = KeyboardButton("Рубли")
btnKz = KeyboardButton("Тенге")
btnUSD = KeyboardButton("Доллары")
btnEUR = KeyboardButton("Евро")
MoneyMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRub,
                                                          btnKz,
                                                          btnUSD,
                                                          btnEUR,
                                                          MainMenu,
                                                          btnMain,)
