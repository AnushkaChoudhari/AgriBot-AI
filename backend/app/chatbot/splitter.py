from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.chatbot.ingest import load_documents
from app.config.settings import CHUNK_SIZE, CHUNK_OVERLAP


def split_documents():
    # Load all PDF documents
    documents = load_documents()

    if not documents:
        print("❌ No documents loaded.")
        return []

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)

    print(f"\n✅ Total Chunks: {len(chunks)}")

    print("\nFirst Chunk:\n")
    print(chunks[0].page_content)

    return chunks


if __name__ == "__main__":
    split_documents()