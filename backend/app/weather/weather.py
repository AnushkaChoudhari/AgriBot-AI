import requests
from app.config.settings import OPENWEATHER_API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str):

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return None

    return response.json()


if __name__ == "__main__":

    weather = get_weather("Pune")

    print(weather)