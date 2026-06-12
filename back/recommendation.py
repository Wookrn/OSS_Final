from fastapi import APIRouter
from model import UserRequest

recommendation_router = APIRouter()

@recommendation_router.post("/recommend")
async def recommend(user_request: UserRequest):
    if user_request.category == "A":
        recommendation = "추천A"
    elif user_request.category == "B":
        recommendation = "추천B"
    else:
        recommendation = "추천C"

    return {
        "category": user_request.category,
        "recommendation": recommendation
    }