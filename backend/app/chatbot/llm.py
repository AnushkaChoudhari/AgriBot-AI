import os
from dotenv import load_dotenv
from google import genai
from app.config.settings import LLM_MODEL
import time

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_llm(prompt: str) -> str:
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt,
            )
            return response.text

        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")

            if attempt < 2:
                time.sleep(3)
            else:
                return "Gemini server is busy. Please try again in a few seconds."