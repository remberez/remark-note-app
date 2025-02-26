from fastapi_users.db import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase
)
from sqlalchemy.ext.asyncio import AsyncSession

from .base import Base, IntegerIDMixin
from ..types.user_id import UserIDType


class UserORM(Base, IntegerIDMixin, SQLAlchemyBaseUserTable[UserIDType]):
    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyUserDatabase(session, cls)
