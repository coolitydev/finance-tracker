from typing import Annotated, Optional

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core import settings, db_helper

from .models import User
from .schemas import UserRead, UserCreate

router = APIRouter(
    prefix=settings.api.v1.user_prefix,
    tags=["Users"],
)
