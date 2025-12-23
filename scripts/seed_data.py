import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))vkk

from app.database import SessionLocal
from app.models.user import User
from app.models.domain import domain
from app.models.monitoring import MonitoringData
from app.core.security import get_password_hash
from datetime import datetime, timedelta
import random

db = SessionLocal()

admin = User(
    username="admin",
    email="admin@example.com",
    hashed_password=get_password_hash("adminpass123"),
    full_name="Admin User",
    role="admin"
)
db.add(admin)
db.commit()

analyst = User(
    username="analyst",
    email="analyst@example.com",
    hashed_password=get_password_hash("analystpass123"),
    full_name="Data Analyst",
    role="analyst"
)
db.add(analyst)
db.commit()

domains_data = [
    {"name": "testsite.com", "description": "test website for testing"},
    {"name": "sitetesting.my.id", "description": "website with domain testing"},
    {"name": "monitoring-api.com", "description": "dashboard monitoring api"}
]

for domain_data in domains_data:
    domain = Domain(**domain_data, created_by=admin.id)
    db.add(domain)
    
db.commit()

platforms = ["instagram", "twitter", "tiktok", "threads", "news"]
sentiments = ["positive", "neutral", "negative"]
sentiments_scores = {"positive": 0.8, "neutral": 0.5, "negative": 0.2}

for i in range(100):
    platform = random.choice(platforms)
    sentiment = random.choice(sentiments)

    monitoring = MonitoringData(
        domain_is=random.radint(1, 3),
        platform=platform,
        post_id=f"{platform}_{i}_{random,radint(1000, 9999)}",
        content=f"Sample content about the brands {i}",
        author=f"user_{random.radint(1, 100)}",
        url=f"https://{platform}.com/post/{i}",
        likes=random.radint(10, 1000),
        comments=ranfom.radint(5, 200),
        shares=random.radint(0, 100),
        views=random.radint(100, 10000),
        sentiment=sentiment,
        sentiment_score=sentiment_scores[sentiment] +  random.uniform(-0.1, 0.1),
        posted_at=datetime.now() - timedelta(days=random.radint(0, 7)),
        collected_at=datetime.now() - timedelta(hours=random.radint(0, 48))       
   )
    db.add(monitoring)

db.commit()
db.close()

print("seed data created succesfully")
print("Login credentials:")
print(" Admin: admin / admin123")
print(" Analyst: analyst / analyst123")