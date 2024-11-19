from fastapi import APIRouter

from core.config import settings

from api.v1.user.router import router as user_router

router = APIRouter(prefix=settings.api.v1.prefix)
router.include_router(user_router)