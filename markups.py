from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton("На главную")

# -----Main Menu-----
btnStocks = KeyboardButton("Цены активов")
btnWeather = KeyboardButton("Узнать погоду")
btnNews = KeyboardButton("Случайная новость")
MainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnStocks, btnWeather, btnNews)

# -----Stocks Menu-----
btnCompany = KeyboardButton("Акции компаний")
btnMoney = KeyboardButton("Традиционные валюты")
btnCrypto = KeyboardButton("Криптовалюты")
StocksMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCompany,
                                                           btnMoney,
                                                           btnCrypto,
                                                           btnMain,)

# -----Company Menu-----
btnAAPL = KeyboardButton("AAPL")
btnAAT = KeyboardButton("AAT")
CompanyMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAAPL,
                                                            btnAAT,
                                                            btnMain,)

# -----Crypto Menu-----
btnBTC = KeyboardButton("BTC")
btnEth = KeyboardButton("Ethereum")
btnSolana = KeyboardButton("Solana")
btnNear = KeyboardButton("Near")
btnTon = KeyboardButton("Ton")
btnUSDT = KeyboardButton("USDT")
CryptoMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnBTC,
                                                           btnEth,
                                                           btnSolana,
                                                           btnNear,
                                                           btnTon,
                                                           btnUSDT,
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
                                                          btnMain,)

# -----Company Menu-----
btnKrasnodar = KeyboardButton("Krasnodar")
btnMoscow = KeyboardButton("Moscow")
CitiesMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnKrasnodar,
                                                           btnMoscow,
                                                           btnMain,)
