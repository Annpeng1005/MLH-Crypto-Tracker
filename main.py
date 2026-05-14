from google import genai
import os
from dotenv import load_dotenv
from crypto_client import get_roster_data, get_url_live, filter_coins_roster, handle_alert
from utils import export_file
from slack import send_to_slack

# Load the .env file
load_dotenv()

gemini_api_key = os.getenv('gemini_api_key')
crypto_api_key = os.getenv('crypto_api_key')

headers = {"Authorization": f"Apikey {crypto_api_key}"}

client = genai.Client(api_key=gemini_api_key)

target_coins = ["bitcoin", "ethereum", "solana", "ripple", "dogecoin"]

roster_data = get_roster_data()


price_data = get_url_live()

filter_coins = filter_coins_roster(roster_data, target_coins)

def analyze_market_data(headers, client):
    alerts = []

    # threshold is flexible for testing
    threshold = -1

    for coin in filter_coins:
        for price_id in price_data:
            if coin['id'] == price_id:
                change = price_data[price_id]['usd_24h_change']
                price = price_data[price_id]['usd']

                if change <= threshold:
                    ai_alert = handle_alert(coin, change, price, headers, client)
                    print(ai_alert)
                    alerts.append(ai_alert)

    return alerts

alerts = analyze_market_data(headers, client)

export_file(alerts)

send_to_slack(alerts)
