import os
from dotenv import load_dotenv
from google import genai
from app.config.settings import LLM_MODEL

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_llm(prompt: str) -> str:
    try:
        response = client.models.generate_content(
    model=LLM_MODEL,
    contents=prompt,
)
        return response.text

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print(ask_llm("What is photosynthesis?"))