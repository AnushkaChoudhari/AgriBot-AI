from fastapi import APIRouter

from app.weather.service import weather_summary

router = APIRouter(prefix="/weather", tags=["Weather"])


@router.get("/{city}")
def get_weather(city: str):

    data = weather_summary(city)

    if data is None:
        return {"error": "City not found"}

    return data