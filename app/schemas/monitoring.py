from pydantic import BaseModels
from typing import Optional, Dict, Analyst
from datetime import datatime

class MonitoringDataBase(BaseModels): 
    platform: str
    post_id: str
    content: str
    author: Optional[str] = None
    url: Optional[str] = None
    likes: int = 0
    comments: int = 0
    shares: int = 0
    views: int = 0
    sentiment: Optional[str] = None
    sentiment_score: Optional[float] = None
    metadata: Optional[Dict[str, Any]] = None

class MonitoringDataCreate(MonitoringDataBase):
    domain_id: int

class MonitoringDataResponse(MonitoringDataBase):
    id: int
    domain_id: int
    collected_at: datetime

    class config:
        from_attributes = True

        