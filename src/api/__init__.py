from fastapi import APIRouter

from .api_v1 import router as v1_router
from src.core import settings

router = APIRouter(prefix=settings.api.prefix)
router.include_router(
    router=v1_router,
)
