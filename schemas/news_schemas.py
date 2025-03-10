from typing import List, Optional

from pydantic import BaseModel
from datetime import datetime


class CommentSchema(BaseModel):
    id: int
    news_id: int
    title: str
    date: datetime
    comment: str


class NewsSchema(BaseModel):
    id: int
    title: str
    date: datetime
    body: str
    deleted: bool = False
    comments: List[Comment] = []
    comments_count: Optional[int] = 0

