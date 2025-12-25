from fastapi import APIRouter

api_router = APIRouter()

# import router di sini, bukan top-level module
from .auth import router as auth_router
from .users import router as users_router
from .domains import router as domains_router
from .monitoring import router as monitoring_router
from .analytics import router as analytics_router

api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(domains_router, prefix="/domains", tags=["Domains"])
api_router.include_router(monitoring_router, prefix="/monitoring", tags=["Monitoring"])
api_router.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])
