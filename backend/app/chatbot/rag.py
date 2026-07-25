from app.chatbot.llm import ask_llm
from app.chatbot.prompts import SYSTEM_PROMPT
from app.chatbot.memory import memory
from app.chatbot.router import detect_intent
from app.tools.rag_tool import search_documents
from app.tools.weather_tool import get_weather_context
from app.tools.prompt_builder import build_prompt


def ask_agribot(question: str) -> str:

    # Save user message
    memory.add_user(question)

    # Conversation history
    history = memory.get_history()

    # Detect intent
    intent = detect_intent(question)

    print("\n========== INTENT ==========")
    print(intent)

    context = ""
    weather = ""

    # ==========================================
    # AGRICULTURE
    # ==========================================
    if intent == "agriculture":

        context = search_documents(question)

        weather = """
Weather Information:
Not required for this question.
"""

    # ==========================================
    # WEATHER
    # ==========================================
    elif intent == "weather":

        context = """
Knowledge Base:
Not required for this question.
"""

        weather = get_weather_context(question)

    # ==========================================
    # WEATHER + AGRICULTURE
    # ==========================================
    elif intent == "weather_agriculture":

        context = search_documents(question)

        weather = get_weather_context(question)

    # ==========================================
    # GENERAL
    # ==========================================
    else:

        context = """
Knowledge Base:
Not required.
"""

        weather = """
Weather Information:
Not required.
"""

    # ==========================================
    # BUILD PROMPT
    # ==========================================
    prompt = build_prompt(
    history=history,
    weather=weather,
    context=context,
    question=question,
)

    print("\n========== FINAL PROMPT ==========\n")
    print(prompt)
    print("\n==================================\n")

    answer = ask_llm(prompt)

    memory.add_bot(answer)

    return answer