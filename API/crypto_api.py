import requests
import pprint
import json
from dotenv import load_dotenv
import os


def get_price(symbol):
    load_dotenv()
    api_key = os.getenv('CRYPTO_API_KEY')

    parameters = {'symbol': symbol}
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': api_key}

    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    res = requests.get(url, params=parameters, headers=headers)
    # print(f"Keys: {res.json().keys()}\n")

    data = res.json()
    # pprint.pprint(data)
    # print()
    price = data["data"][symbol]["quote"]["USD"]["price"]
    slug = data["data"][symbol]["name"]

    return f"Price of the {slug}: {price}"


symbol = input("Enter a cryptocurrency symbol: ").upper()
print(get_price(symbol))
