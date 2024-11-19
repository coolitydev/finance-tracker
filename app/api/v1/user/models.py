from datetime import datetime

from sqlalchemy import String, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column

from core.base import Base


class User(Base):
    __tablename__ = 'users'

    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
