import requests
import pprint
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('OPEN_AI_API')
BASE_URL = f"https://api.openweathermap.org/data/2.5/weather"


def fetch_data(api_key, base_url):
    city = input("Enter a city: ")
    request_url = f"{base_url}?appid={api_key}&q={city}"

    response = requests.get(request_url)

    if response.status_code == 200:
        print("Data fetched successfully\n")
        my_data = response.json()
        # print(my_data.keys())
        pprint.pprint(my_data)

    else:
        print("An error occurred")


fetch_data(API_KEY, BASE_URL)
