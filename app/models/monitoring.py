from sql import Column, Integer, String, Text, Float, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class MonitoringData(Base):
    __tablename__ = "monitoring_data"

    id = Column(Integer, primary_key=True, index=True)
    domain_id = Column(Integer, ForeignKey(domains.id))
    platform = Column(String, index=True)
    post_id = Column(String, unique=True, index=True)
    content = Column(Text)
    author = Column(String)
    url = Column(String)

    likes = Column(Integer, default=0)
    comments = Column(Integer, default=0)
    shares = Column(Integer, default=0)
    views = Column(Integer, default=0)

    sentiment = Column(String)
    sentiment_score = Column(Float)

    metadata = Column(JSON)
    posted_at = Column(DateTime(timezone=True))
    collected_at = Column(DateTime(timezone=True), server_default=func.now())

    domain = relationship("Domain", back_populates="monitoring_data")
