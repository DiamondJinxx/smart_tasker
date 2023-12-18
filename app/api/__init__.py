from fastapi import APIRouter
from .endpoints import init

api_router = APIRouter()
api_router.include_router(init.router, tags=["Init application"])

__all__ = (
    "api_router",
)
