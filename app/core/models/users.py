from datetime import datetime

from fastapi_users.db import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import (
    Mapped, relationship
)
from sqlalchemy.testing.schema import mapped_column

from .base import (
    Base, IntegerIDMixin
)
from core.types.user_id import UserIDType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .notes import NoteORM


class UserORM(Base, IntegerIDMixin, SQLAlchemyBaseUserTable[UserIDType]):
    premium_end_date: Mapped[datetime] = mapped_column(nullable=True)

    notes: Mapped["NoteORM"] = relationship(back_populates="user")

    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyUserDatabase(session, cls)
