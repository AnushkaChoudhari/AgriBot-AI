def detect_intent(question: str):

    question = question.lower()

    weather_keywords = [
        "weather",
        "temperature",
        "rain",
        "humidity",
        "wind",
        "forecast",
        "today",
        "tomorrow"
    ]

    agriculture_keywords = [
        "spray",
        "fungicide",
        "irrigate",
        "irrigation",
        "harvest",
        "crop",
        "disease",
        "symptom",
        "fertilizer",
        "soil",
        "leaf",
        "black rot",
        "powdery mildew"
    ]

    has_weather = any(word in question for word in weather_keywords)
    has_agriculture = any(word in question for word in agriculture_keywords)

    if has_weather and has_agriculture:
        return "weather_agriculture"

    elif has_weather:
        return "weather"

    elif has_agriculture:
        return "agriculture"

    else:
        return "general"

if __name__ == "__main__":

    tests = [
        "Should I spray fungicide today in Pune?",
    ]

    for t in tests:
        print(t)
        print(detect_intent(t))
        print()