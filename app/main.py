from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.api.routes import router as include_router

try:
    from app.api.routes import router as infrastructure_router
    HAS_INFRA_ROUTER = True
except ImportError:
    HAS_INFRA_ROUTER = False

from app.api.v1 import api_router as v1_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bigdata Media Intelegence API",
    description="APi Infrastucture managements",
    version="2.0.0"
)

##CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {
        "message": "Bigdata Media Intellegence APi",
        "version": "2.0.0",
        "docs": "/docs",
        "infrastructure": "/api/v1/infrastructure",
        "media": "/api/v1"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "media-intelligence"}

##router

if HAS_INFRA_ROUTER:
    app.include_router(infrastructure_router, prefix="/api/v1/infrastructure")

app.include_router(v1_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=70000)