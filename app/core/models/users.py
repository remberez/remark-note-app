from fastapi_users.db import SQLAlchemyBaseUserTable
from .base import Base, IntegerIDMixin


class UserORM(Base, IntegerIDMixin, SQLAlchemyBaseUserTable[int]):
    ...
