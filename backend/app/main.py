from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.weather import router as weather_router

app = FastAPI(
    title="AgriBot AI",
    version="1.0"
)

app.include_router(chat_router)
app.include_router(weather_router)

