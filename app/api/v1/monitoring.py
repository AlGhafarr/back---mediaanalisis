from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.user import User
from app.schemas.monitoring import MonitoringDataResponse
from app.models.monitoring import MonitoringData
from app.core.security import get_current_active_user

router = APIRouter()


@router.get("/", response_model=List[MonitoringDataResponse])
def list_monitoring_data(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """List monitoring data"""
    data = db.query(MonitoringData).offset(skip).limit(limit).all()
    return data


@router.get("/stats")
def get_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get monitoring statistics"""
    total = db.query(MonitoringData).count()
    return {
        "total_posts": total,
        "platforms": ["instagram", "twitter", "tiktok", "threads", "news"]
    }