from sqlalchemy.orm import Session
from typing import List, Optional
from models.models import NewsModel
from schemas.news_schemas import NewsSchema


class NewsRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all_news(self) -> List[NewsModel]:
        return self.db.query(NewsModel).filter(NewsModel.deleted == False).all()

    def get_news_by_id(self, news_id: int) -> Optional[NewsModel]:
        return self.db.query(NewsModel).filter(NewsModel.id == news_id, NewsModel.deleted == False).first()
