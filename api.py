import requests
from random import randint


def collect_stocks_data(token_stocks: str, ticker: str, exchange="NASDAQ", interval="1min") -> str:
    result = requests.get(f"https://api.twelvedata.com/time_series?symbol={ticker}:{exchange}"
                          f"&interval={interval}&apikey={token_stocks}")
    try:
        if result.status_code == 200:
            result = result.json()
            message_text = "Мета информация:\n"
            for k, v in result["meta"].items():
                message_text += k + " : " + v + "\n"
            message_text += "\nДанные актива: \n"
            for k, v in result["values"][0].items():
                message_text += k + " : " + v + "\n"
            return message_text
        else:
            return "Мне не удалось заполучить данные об этом активе"
    except Exception as e:
        print("!Something went wrong: ", e)
        return "Я не смог собрать полные данные"


def collect_weather_data(token_weather: str, city: str) -> str:
    return "В разработке ⚒️"


def collect_random_news(token_news: str) -> str:
    result = requests.get(f"https://newsapi.org/v2/everything?q=Apple&from="
                          f"2022-07-11&sortBy=popularity&apiKey={token_news}")
    try:
        if result.status_code == 200:
            data = result.json()["articles"][randint(0, 100)]
            return "Заголовок: " + str(data["title"]) + "\n" +\
                   "Автор: " + str(data["author"]) + "\n" + \
                   "Ссылка на новость: " + str(data["url"])
        else:
            return "Новостей пока нет"
    except Exception as e:
        print("!Something went wrong: ", e)
        return "Мне не удалось получить новости"
