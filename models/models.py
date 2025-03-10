from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class NewsModel(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    date = Column(DateTime, default=func.now())
    body = Column(String)
    deleted = Column(Boolean, default=False)
    comments = relationship("Comment", back_populates="news", cascade="all, delete-orphan")

    @property
    def comments_count(self) -> int:
        return len(self.comments)


class CommentModel(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    news_id = Column(Integer, ForeignKey("news.id"), nullable=False)
    title = Column(String, nullable=False)
    date = Column(DateTime, default=func.now())
    comment = Column(String)

    news = relationship("News", back_populates="comments")