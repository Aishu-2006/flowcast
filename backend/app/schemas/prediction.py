from pydantic import BaseModel


class PredictionRequest(BaseModel):
    place_id: int
    service_type: str
    hour: int
    day_of_week: int