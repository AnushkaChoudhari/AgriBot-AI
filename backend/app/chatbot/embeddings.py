from langchain_huggingface import HuggingFaceEmbeddings
from app.config.settings import EMBEDDING_MODEL

def get_embeddings():
   

    embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)
    return embeddings


if __name__ == "__main__":
    model = get_embeddings()
    print("✅ Embedding model loaded successfully!")