from fastapi import APIRouter
from app.api.v1 import auth, users, domains, monitoring, analytics

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(domains.router, prefix="/domains", tags=["Domains"])
api_router.include_router(monitoring.router, prefix="/monitoring", tags=["Monitoring"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])