from fastapi import APIRouter

from src.core import settings


router = APIRouter(
    prefix=settings.api.v1.prefix,
)