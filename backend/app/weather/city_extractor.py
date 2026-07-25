import re

def extract_city(question: str):
    """
    Extract city name from the user's question.
    Example:
    'Should I irrigate today in Pune?'
    -> Pune
    """

    match = re.search(r"\bin\s+([A-Za-z\s]+)", question, re.IGNORECASE)

    if match:
        return match.group(1).strip()

    return None


if __name__ == "__main__":

    print(extract_city("Should I spray fungicide today in Pune?"))
    print(extract_city("Should I irrigate tomorrow in Nashik?"))
    print(extract_city("How do I control grape black rot?"))