from app.chatbot.retriever import get_retriever
from app.chatbot.llm import ask_llm
from app.chatbot.prompts import SYSTEM_PROMPT
from app.chatbot.memory import memory

retriever = get_retriever()


def ask_agribot(question: str) -> str:

    memory.add_user(question)

    # Retrieve relevant documents
    docs = retriever.invoke(question)

    # Print retrieved documents
    print("\n========== RETRIEVED DOCUMENTS ==========\n")

    for i, doc in enumerate(docs, start=1):
        print(f"\n----- Document {i} -----")
        print(doc.page_content[:500])

    # Combine retrieved text into one context
    context = "\n\n".join(doc.page_content for doc in docs)

    # Get conversation history
    history = memory.get_history()

    # Build prompt
    prompt = f"""
{SYSTEM_PROMPT}

=========================
CONVERSATION HISTORY
=========================

{history}

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

    # Ask Gemini
    answer = ask_llm(prompt)

    # Save bot response
    memory.add_bot(answer)

    return answer


if __name__ == "__main__":

    while True:

        question = input("\nYou: ")

        if question.lower() == "exit":
            break

        answer = ask_agribot(question)

        print("\nAgriBot:\n")
        print(answer)