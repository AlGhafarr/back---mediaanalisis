from pydantic_settings import BaseSettings
from typing import Optional
import secrets

class Settings(BaseSettings):
    """Application settings."""
    
    APP_NAME: str = "Bigdata Media Intelligence"
    APP_VERSION: str = " 2.0.0"
    DEBUG: bool = True

    ##security
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "H256"
    ACESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str = "postgresql://bigdata_user:bigdata_password@localhost:5432/bigdata"
    SQL_ECHO: bool = False
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/2"
    
    # CORS
    CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:5174"]
    
#    # Infrastructure
#    AWS_REGION: str = "us-east-1"
#    AWS_ACCESS_KEY_ID: str = ""
#    AWS_SECRET_ACCESS_KEY: str = ""
    
    # Domain Management
#    DOMAIN_PROVIDER: str = "route53"  # route53, cloudflare, etc.
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
