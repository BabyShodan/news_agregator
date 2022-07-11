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
    result = requests.get(f"https://api.weatherapi.com/v1/current.json?key={token_weather}&q={city}&aqi=no")
    try:
        if result.status_code == 200:
            result = result.json()
            result.pop("condition", "")
            # Доделать и оптимизировать
            elements = ["location", "current"]
            answer = ""
            for i in elements:
                answer += i + "\n"
                for k, v in result[i].items():
                    answer += k + " : " + v + "\n"
            return answer
        else:
            return "Мне не удалось получить данные о погоде"
    except Exception as e:
        print("!Something went wrong: ", e)
        return "Нет данных о текущей погоде"


def collect_random_news(token_news: str) -> str:
    result = requests.get(f"https://newsapi.org/v2/everything?q=Apple&from="
                          f"2022-07-11&sortBy=popularity&apiKey={token_news}")
    try:
        if result.status_code == 200:
            result = result.json()["articles"][randint(0, 100)]
            return "Заголовок: " + str(result["title"]) + "\n" +\
                   "Автор: " + str(result["author"]) + "\n" + \
                   "Ссылка на новость: " + str(result["url"])
        else:
            return "Новостей пока нет"
    except Exception as e:
        print("!Something went wrong: ", e)
        return "Мне не удалось получить новости"
