from fastapi import FastAPI
from .routes import news

app = FastAPI()

app.include_router(news.router, prefix="/api", tags=["news"])


@app.get("/")
async def root():
    return {"message": "｡ ₊°༺❤︎༻°₊ ｡ Welcome to the News API, sweetie! ｡ ₊°༺❤︎༻°₊ ｡"}
