from pathlib import Path
import os
from dotenv import load_dotenv

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[3]
BACKEND_DIR = PROJECT_ROOT / "backend"

# Load environment variables
load_dotenv(BACKEND_DIR / ".env")

# Important Paths
DOCS_PATH = PROJECT_ROOT / "docs"
VECTOR_DB_PATH = PROJECT_ROOT / "vector_db"
UPLOADS_PATH = BACKEND_DIR / "app" / "uploads"

# AI Models
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_PROVIDER = "gemini"
LLM_MODEL = "gemini-2.5-flash-lite"

# Text Splitting
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# Retrieval
TOP_K = 4

# Weather API
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")