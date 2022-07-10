import requests


def collect_stocks_data(token_stocks: str, ticker: str, exchange="NASDAQ", interval="1min") -> tuple:
    result = requests.get(f"https://api.twelvedata.com/time_series?symbol={ticker}:{exchange}"
                          f"&interval={interval}&apikey={token_stocks}").json()
    return result["meta"], result["values"][0]


def collect_weather_data(token_weather: str, city: str) -> str:
    pass
