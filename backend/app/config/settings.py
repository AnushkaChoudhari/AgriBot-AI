from pathlib import Path

# Project Root (AgriBot-AI/)
BASE_DIR = Path(__file__).resolve().parents[3]

# Important Paths
DOCS_PATH = BASE_DIR / "docs"
VECTOR_DB_PATH = BASE_DIR / "vector_db"
UPLOADS_PATH = BASE_DIR / "backend" / "app" / "uploads"

# AI Model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Text Splitting
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# Retrieval
TOP_K = 4

LLM_PROVIDER = "gemini"
LLM_MODEL = "gemini-2.5-flash-lite"