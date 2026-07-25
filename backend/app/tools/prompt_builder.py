from app.chatbot.prompts import SYSTEM_PROMPT


def build_prompt(
    history: str,
    weather: str,
    context: str,
    question: str,
) -> str:
    """
    Builds the final prompt sent to Gemini.
    """

    prompt = f"""
{SYSTEM_PROMPT}

=========================
CONVERSATION HISTORY
=========================

{history}

=========================
CURRENT WEATHER
=========================

{weather}

=========================
KNOWLEDGE BASE
=========================

{context}

=========================
USER QUESTION
=========================

{question}

=========================
ANSWER
=========================
"""

    return prompt