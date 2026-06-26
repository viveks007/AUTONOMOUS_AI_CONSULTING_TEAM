import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city: str):

    url = "http://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": city
    }

    response = requests.get(url, params=params)

    response.raise_for_status()

    data = response.json()

    current = data["current"]

    location = data["location"]

    return {
        "city": location["name"],
        "country": location["country"],
        "temperature": current["temp_c"],
        "condition": current["condition"]["text"],
        "humidity": current["humidity"],
        "wind_kph": current["wind_kph"]
    }