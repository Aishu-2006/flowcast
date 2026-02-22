from fastapi import APIRouter
from app.schemas.prediction import PredictionRequest
from app.services.prediction_service import predict_visit

router = APIRouter()


@router.post("/predict")
def get_prediction(data: PredictionRequest):
    result = predict_visit(
        data.place_id,
        data.service_type,
        data.hour,
        data.day_of_week
    )
    return result