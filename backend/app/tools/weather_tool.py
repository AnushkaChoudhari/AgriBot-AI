from app.weather.city_extractor import extract_city
from app.weather.advisor import get_weather_advice


def get_weather_context(question: str) -> str:
    """
    Extract the city from the user's question and
    return formatted weather information.
    """

    city = extract_city(question)

    print("\n========== CITY ==========")
    print(city)

    if city:
        weather = get_weather_advice(city)
    else:
        weather = """
No weather information available because the user did not specify a city.
"""

    print("\n========== WEATHER ==========\n")
    print(weather)

    return weather


if __name__ == "__main__":

    question = "Should I spray fungicide today in Pune?"

    weather = get_weather_context(question)

    print("\n========== RETURNED WEATHER ==========\n")
    print(weather)