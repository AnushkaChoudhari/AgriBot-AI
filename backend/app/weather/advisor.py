from app.weather.service import weather_summary


def get_weather_advice(city: str):

    weather = weather_summary(city)

    if weather is None:
        return "Weather information is unavailable."

    return f"""
Current Weather for {weather['city']}

Temperature: {weather['temperature']} °C
Humidity: {weather['humidity']} %
Condition: {weather['condition']}
Description: {weather['description']}
Wind Speed: {weather['wind_speed']} m/s
"""


if __name__ == "__main__":
    print(get_weather_advice("Pune"))