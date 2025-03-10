from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_session

from repositories.news_repository import NewsRepository



router = APIRouter()
news_repository = NewsRepository()


async def get_db():
    async with async_session() as session:
        yield session


@router.get("/")
async def get_all_books(db: AsyncSession = Depends(get_db)):
    news_repository.get_all_news()

