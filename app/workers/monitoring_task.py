from celery import shared_task
from sqlalchemy.orms import Session
from app.database import SessionLocal
from app.models.monitoring import MonitoringData
from app.models.domain import domain
from datetime import datetime
import requests
from textblob import TextBlob
import logging

logger = logging.getLogger(__name__)

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

def analyze_sentiment(text: str) -> tuple[str, float]:
    try:
        blob: TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0.1:
            sentiment = "positive"
        elif polarity < -0.1:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        score = (polarity + 1) / 2

        return sentiment, score
    except Exception as e:
        logger.error(f"Sentiment analysis failed: {e}")
        return "neutral", 0.5

@shared_task(name="monitoring_instagram")
def monitoring_instagram(domain_id: int, keywords: list):
    db = get_db()
    try:
        mock_posts = [
            {
                "post+id": f"ig_{domain_id}_{datetime.now().timestamp()}",
                "content": f"Great product from domain {domain_id}! #amazing",
                "author": "user123",
                "url": "https://instagram.com/p/ig_post_example",
                "Likes": 150,
                "comments": 25,
                "shares": 10,
                "created_at": datetime.now()
            }
        ]

        for post in mock_posts:
            sentiment, score = analyze_sentiment(post["content"])

            monitoring_data = MonitoringData(
                domain_id=domain_id,
                platform="instagram",
                post_id=post["post_id"],
                content=post["content"],
                author=post["author"],
                url=post["url"],
                likes=post["likes"],
                comments=post["comments"],
                shares=post["shares"],
                sentiment=sentiment,
                sentiment_score=score,
                posted_at=post["posted_at"]
            )

            db.add(monitoring_data)
        
        db.commit()
        logger.info(f"Instagram monitoring for domain {domain_id} completed successfully.")

    except Exception as e:
        logger.error(f"Instagram monitoring error: {e}")
        db.rollback()
    finally:
        db.close()

@shared_task(name="monitoring_twitter")
def monitoring_twitter(domain_id: int, keywords: list):
    db = get_db()

    try:

        mock_tweets = [
            {
                "post_id": f"tw_{domain_id}_{datetime.now().timestamp()}",
                "content": f"just discovered an amazing service {keywords[0] if keywords else ''}",
                "author": "twitter_user",
                "url": "https://twitter.com/user/status/example",
                "likes": 200,
                "comments": 15,
                "shares": 45,
                "posted_at": datetime.now()
            }
        ]

        for tweer in mock_tweets:
            sentiment, score = analyze_sentiment(tweet["content"])

            monitoring_data = MonitoringData(
                domain_id=domain_id,
                platform="twitter",
                post_id=tweet["post_id"],
                content=tweet["content"],
                author=tweet["author"],
                url=tweet["url"],
                likes=tweet["likes"],
                comments=tweet["comments"],
                shares=tweet["shares"],
                sentiment=sentiment,
                sentiment_score=score,
                posted_at=tweet["posted_at"]
            )

            db.add(monitoring_data)
        
        db.commit()
        logger.info(f"Twitter monitoring completed for domain {domain_id}")

    except Exception as e:
        logger.error(f"Twitter monitoring error: {e}")
        db.rollback()
    finally:
        db.close()

@shared_task(name="monitoring_tiktok")
def monitoring_tiktok(domain_id: int, keywords: list):
    db.get_db()

    try:
        mock_videos = [
            {
                "post_id": f"tt_{domain_id}_{datetime.now().timestamp()}",
                "content": f"Check out this cool thing! {keywords[0] if keywords else ''}",
                "author": "tiktok_creator",
                "url": "https://tiktok.com/@user/video/example",
                "likes": 1200,
                "comments": 89,
                "shares": 156,
                "views": 15000,
                "posted_at": datetime.now()
            }
        ]

        for video in mock_videos:
            sentiment, score = analyze_sentiment(video["content"])

            monitoring_data = MonitoringData(
                domain_id=domain_id,
                platform="tiktok",
                post_id=video["post_id"],
                content=video["content"],
                author=video["author"],
                url=video["url"],
                likes=video["likes"],
                comments=video["comments"],
                shares=video["shares"],
                views=video["views"],
                sentiment=sentiment,
                sentiment_score=score,
                posted_at=video["posted_at"]
            )

            db.add(monitoring_data)

        db.commit()
        logger.info(f"Tiktok monitoring completed for domain {domain_id}")

    except Exception as e:
        logger.error(f"Tiktok monitoring error: {e}")
        db.rollback()
    finally:
        db.close()

@shared_task(name="monitoring_news")
def monitoring_news(domain_id: int, keywords: list):

    db = get_db()

    try:
        mock_articles = [
            {
                "post_id": f"news_{domain_id}_{datetime.now().timestamp()}",
                "content": f"Breaking: New development in {keywords[0] if keywords else 'industry'}",
                "author": "News Reporter",
                "url": "https://newssite.com/article/example",
                "views": 5000,
                "posted_at": datetime.now()
            }
        ]

        for article in mock_articles:
            sentiment, score = analyze_sentiment(articlep["content"])

            monitoring_data = MonitoringData(
                domain_id=domain_id,
                platform="news",
                post_id=article["post_id"],
                content=article["content"],
                author=article["author"],
                url=article["url"],
                views=article["views"],
                sentiment=sentiment,
                sentiment_score=score,
                posted_at=article["posted_at"]
            )

            db.add(monitoring_data)

        db.commit()
        logger.info(f"News monitoring completed for domain {domain_id}")

    except Exception as e:
        logger.error(f"News monitoring error: {e}")
        db.rollback()
    finally:
        db.close()

@shared_task(name="monitoring_all_platforms")
def monitoring_all_platforms(domain_id: int, keywords: list):
    logger.info(f"Starting monitoring for domain {domain_id} with keywords {keywords}")

    monitoring_instagram.delay(domain_id, keywords)
    monitoring_twitter.delay(domain_id, keywords)
    monitoring_tiktok.delay(domain_id, keywords)
    monitoring_news.delay(domain_id, keywords)

    return f"Monitoring initiated for domain {domain_id}"

from celery.scheduler import crontab

app.conf.beat_schedule = {
    'monitoring-all-domain-everty-hour': {
        'task': 'monitoring_all_domains',
        'schedule': crontab(minute=0)
    },
}
@shared_task(name="monitoring_all_domains")
def monitoring_all_domains():
    db = SessionLocal()
    try:
        domains = db.query(domain).filter(Domain.status == 'active').all()

        for domain in domains:
            keywords = [domain.name]
            monitoring_all_platforms.delay(domain.id, keywords)
        finally:
            db.close()