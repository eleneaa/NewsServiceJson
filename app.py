from fastapi import FastAPI
from routing.news import router as news_routing

app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

app.include_router(news_routing)