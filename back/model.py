from pydantic import BaseModel

class UserRequest(BaseModel):
    play_style: str
    game_type: str