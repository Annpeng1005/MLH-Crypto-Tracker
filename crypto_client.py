import requests
import time
from ai_agent import make_ai_alert

def get_roster_data():
    url_roster = "https://api.coingecko.com/api/v3/coins/list"

    roster_response = requests.get(url_roster)
    roster_data = roster_response.json()

    return roster_data

def get_url_live():

    url_live = "https://api.coingecko.com/api/v3/simple/price"

    price_params = {'ids': 'bitcoin,ethereum,solana,ripple,dogecoin',
                    'vs_currencies': 'usd',
                    'include_24hr_change': True
                    }

    price_response = requests.get(url_live, params=price_params)
    price_data = price_response.json()

    return price_data

def filter_coins_roster(roster_data, target_coins):
    filter_coins = []
    for el in roster_data:
        if el['id'] in target_coins:
            filter_coins.append(el)
    return filter_coins

def get_news(coin_symbol, headers):
    time.sleep(2)
    base_news_url = "https://min-api.cryptocompare.com/data/v2/news"
    news_url = f"{base_news_url}/?lang=EN&categories={coin_symbol}"
    news_response = requests.get(news_url, headers=headers)
    news_data = news_response.json()

    return news_data

def get_top_headlines(news_data):
    # at least 3 news or the minimum news that's accessable
    top_3_news = []
    number_of_news_items = min(3, len(news_data["Data"]))
    for i in range(number_of_news_items):
        top_3_news.append(news_data["Data"][i]["title"])

    return top_3_news

def handle_alert(coin, change, price, headers, client):
    coin_symbol = coin["symbol"].upper()
    news_data = get_news(coin_symbol, headers)
    top_3_news = get_top_headlines(news_data)
    ai_alert = make_ai_alert(coin["name"], change, price, top_3_news, client)

    return ai_alert