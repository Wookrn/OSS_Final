from fastapi import FastAPI
import uvicorn
from recommendation import recommendation_router

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to the Recommendation API"}

app.include_router(recommendation_router)

if(__name__ == "__main__"):
    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True)