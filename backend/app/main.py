from fastapi import FastAPI
from app.api.chat import router as chat_router

app = FastAPI(
    title="AgriBot AI",
    version="1.0"
)

app.include_router(chat_router)

@app.get("/")
def home():
    return {"message": "AgriBot API is running"}