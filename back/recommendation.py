from fastapi import APIRouter
from model import UserRequest

recommendation_router = APIRouter()

@recommendation_router.post("/recommend")
async def recommend(data: UserRequest):
    if (
        data.play_style == "혼자" and data.game_type == "경쟁"
    ):
        recommendation = "싱글 플레이 RPG"
    elif (
        data.play_style == "혼자" and data.game_type == "협력"
    ):
        recommendation = "생존 크래프팅 게임"
    elif (
        data.play_style == "함께" and data.game_type == "경쟁"
    ):
        recommendation = "MOBA, FPS"
    elif (
        data.play_style == "함께" and data.game_type == "협력"
    ):
        recommendation = "협동 멀티 플레이 게임"
    else:
        recommendation = "캐주얼 게임"

    return {
        "play_style": data.play_style,
        "game_type": data.game_type,
        "recommendation": recommendation
    }