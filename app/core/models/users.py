from fastapi_users.db import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase
)
from sqlalchemy.ext.asyncio import AsyncSession

from .base import Base, IntegerIDMixin


class UserORM(Base, IntegerIDMixin, SQLAlchemyBaseUserTable[int]):
    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyUserDatabase(session, cls)
