from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession
from .abc_repository import AbstractRepository


class SQLAlchemyAbstractRepository[Model](AbstractRepository[Model], ABC):
    """
    Интерфейс SQLAlchemy репозитория, от которого должны наследоваться все репозитории,
    которые будут использовать SQLAlchemy ORM.
    """
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
