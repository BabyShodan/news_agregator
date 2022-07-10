import requests


def collect_stocks_data(token: str, ticker: str, exchange="NASDAQ", interval="1min") -> tuple:
    result = requests.get(f"https://api.twelvedata.com/time_series?symbol={ticker}:{exchange}"
                          f"&interval={interval}&apikey={token}").json()
    return result["meta"], result["values"][0]
