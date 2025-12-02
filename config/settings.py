from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings."""
    
    # API
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOAD: bool = True
    API_TITLE: str = "Big Data Backend API"
    API_VERSION: str = "0.1.0"
    
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/bigdata"
    SQL_ECHO: bool = False
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/2"
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8080"]
    
    # Infrastructure
    AWS_REGION: str = "us-east-1"
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    
    # Domain Management
    DOMAIN_PROVIDER: str = "route53"  # route53, cloudflare, etc.
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
