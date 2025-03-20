from fastapi import APIRouter, HTTPException
from ..schemas import News, NewsList, Comment
from ..utils import load_json, get_comments_count

router = APIRouter()

news_data = load_json('data/news.json')
comments_data = load_json('data/comments.json')


@router.get("/", response_model=NewsList)
def get_all_news():
    news_list = []
    for news in news_data["news"]:
        if not news["deleted"]:
            news_copy = news.copy()
            news_copy["comments_count"] = get_comments_count(news["id"], comments_data["comments"])
            news_list.append(news_copy)

    return {"news": news_list, "news_count": len(news_list)}


@router.get("/news/{news_id}", response_model=News)
def get_news_by_id(news_id: int):
    current_news = next((news for news in news_data["news"]
                         if news['id'] == news_id and not news["deleted"]), None)

    if current_news is None:
        raise HTTPException(status_code=404, detail=f"News with id={news_id} not found")

    current_news_copy = current_news.copy()
    current_news_copy['comments'] = [
        Comment(**comment) for comment in comments_data['comments']
        if comment['news_id'] == id
    ]
    current_news_copy['comments_count'] = len(current_news_copy['comments'])

    return current_news_copy
