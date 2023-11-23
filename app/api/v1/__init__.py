from fastapi import APIRouter
from .endpoints import metars

# Setup v1 API router to read metars
api_router = APIRouter()
api_router.include_router(metars.router, prefix="/v1", tags=["metars"])
