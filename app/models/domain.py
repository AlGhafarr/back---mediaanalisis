from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class MediaDomain(Base):
    __tablename__ = "media_domains"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True, nullable=False)
    description = Column(String(1000))
    status = Column(String(255), default="active")
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True),  server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    monitoring_data = relationship(
        "MonitoringData",
        back_populates="domain",
        cascade="all, delete-orphan"
    )

