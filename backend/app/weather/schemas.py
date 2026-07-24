from pydantic import BaseModel


class WeatherResponse(BaseModel):
    city: str
    temperature: float
    humidity: int
    condition: str
    description: str
    wind_speed: float