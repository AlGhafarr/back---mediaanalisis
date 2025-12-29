from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class MonitoringData(Base):
    __tablename__ = "monitoring_data"

    id = Column(Integer, primary_key=True, index=True)
    domain_id = Column(Integer, ForeignKey("media_domains.id", ondelete="CASCADE"))
    platform = Column(String(50), index=True, nullable=False)
    post_id = Column(String(255), unique=True, index=True, nullable=False)
    content = Column(Text)
    author = Column(String(255))
    url = Column(String(1000))

    likes = Column(Integer, default=0)
    comments = Column(Integer, default=0)
    shares = Column(Integer, default=0)
    views = Column(Integer, default=0)

    sentiment = Column(String(50))
    sentiment_score = Column(Float)

    meta_data = Column(JSON)
    posted_at = Column(DateTime(timezone=True))
    collected_at = Column(DateTime(timezone=True), server_default=func.now())

    domain = relationship("MediaDomain", back_populates="monitoring_data")
