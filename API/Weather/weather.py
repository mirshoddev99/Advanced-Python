import requests
import pprint
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

country_city = input("Enter a city or country name: ")
BASE_URL = "http://api.weatherapi.com/v1/current.json?key="

req_url = f"{BASE_URL}{API_KEY}&q={country_city}&aqi=yes"
response = requests.get(req_url)

my_data = response.json()
# pprint.pprint(my_data)
# print(my_data.keys())


def print_data():
    # checking status code and type data of response
    if response.status_code == 200 and response.headers['Content-Type'] == "application/json":
        print(f"\t\t\n........The Weather forecast........")

        info = f"""
            County: {my_data['location']['country']}
            City: {my_data['location']['name']}
            Temperature: {my_data['current']['temp_c']} celsius
            Temperature: {my_data['current']['temp_f']} fahrenheit
            The weather condition: {my_data['current']['condition']['text']}
            Humidity: {my_data['current']['humidity']}
            Cloud: {my_data['current']['cloud']}
            """
        print(info)

    else:
        print("An error occurred!\n")


print_data()


# Downloading an image of the weather of a particular city
def download_img():
    city = my_data['location']['name']
    img_url = my_data['current']['condition']['icon']

    img = requests.get(f"http:{img_url}")
    # print(img.content)

    with open(f"{city}.png", "wb") as f:
        f.write(img.content)
        print(f"The image of the weather of {city} was downloaded successfully!")

# download_img()
