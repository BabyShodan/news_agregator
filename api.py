import requests
from exceptions import RequestApiError


def collect_stocks_data(token_stocks: str, ticker: str, exchange="NASDAQ", interval="1min") -> str:
    try:
        result = requests.get(f"https://api.twelvedata.com/time_series?symbol={ticker}:{exchange}"
                              f"&interval={interval}&apikey={token_stocks}")
        data = result.json()
    except RequestApiError as e:
        print("Something went wrong: ", e)
        return "К сожалению я не могу найти данный актив. "
    print(result.status_code)
    if result.status_code == 200:
        message_text = "Мета информация:\n"
        for k, v in data["meta"].items():
            message_text += k + " : " + v + "\n"
        message_text += "\nДанные актива: \n"
        for k, v in data["values"][0].items():
            message_text += k + " : " + v + "\n"
        return message_text
    else:
        return "Мне не удалось заполучить данные об этом активе"


def collect_weather_data(token_weather: str, city: str) -> str:
    return "В разработке ⚒️"


def collect_random_news(token_news: str) -> str:
    return "В разработке ⚒️"
