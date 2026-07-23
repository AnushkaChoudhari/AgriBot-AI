from langchain_community.vectorstores import FAISS

from app.chatbot.embeddings import get_embeddings
from app.config.settings import VECTOR_DB_PATH, TOP_K


def get_retriever():
    print("🧠 Loading embedding model...")
    embeddings = get_embeddings()

    print("📦 Loading vector database...")
    vectorstore = FAISS.load_local(
        str(VECTOR_DB_PATH),
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": TOP_K}
    )

    return retriever


if __name__ == "__main__":
    retriever = get_retriever()

    while True:
        question = input("\nAsk a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        docs = retriever.invoke(question)

        print("\nTop Matching Chunks:\n")

        for i, doc in enumerate(docs, start=1):
            print("=" * 70)
            print(f"Result {i}")
            print("=" * 70)
            print(doc.page_content[:500])
            print()