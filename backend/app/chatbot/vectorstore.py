from langchain_community.vectorstores import FAISS

from app.chatbot.splitter import split_documents
from app.chatbot.embeddings import get_embeddings
from app.config.settings import VECTOR_DB_PATH


def create_vectorstore():
    print("✂️ Splitting documents...")
    chunks = split_documents()

    print("🧠 Loading embedding model...")
    embeddings = get_embeddings()

    print("📦 Creating vector database...")
    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    VECTOR_DB_PATH.mkdir(parents=True, exist_ok=True)

    vectorstore.save_local(str(VECTOR_DB_PATH))

    print(f"\n✅ Saved vector database to:\n{VECTOR_DB_PATH}")


if __name__ == "__main__":
    create_vectorstore()