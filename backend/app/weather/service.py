from app.weather.weather import get_weather


def weather_summary(city: str):

    data = get_weather(city)

    if data is None:
        return None

    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["main"],
        "description": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"]
    }


if __name__ == "__main__":
    print(weather_summary("Pune"))