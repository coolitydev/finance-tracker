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


@router.post("/", response_model=UserRead)
async def create_user(
        user_data: UserCreate,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    user = User(**user_data.model_dump())
    session.add(user)
    await session.commit()
    return user


@router.get("/{user_id}", response_model=Optional[UserRead])
async def get_user(
        user_id: int,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    stmt = select(User).where(User.id == user_id)
    result = await session.execute(stmt)
    return result.scalars().first()
