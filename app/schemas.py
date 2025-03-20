from pydantic import BaseModel
from typing import List, Optional


class Comment(BaseModel):
    id: int
    news_id: int
    title: str
    date: str
    comment: str


class News(BaseModel):
    id: int
    title: str
    date: str
    body: str
    deleted: bool
    comments_count: Optional[int] = 0
    comments: Optional[List[Comment]] = []


class NewsList(BaseModel):
    news: List[News]
    news_count: int
