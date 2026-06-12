from pydantic import BaseModel

class UserRequest(BaseModel):
    category: str