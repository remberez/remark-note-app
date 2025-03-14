from abc import ABC, abstractmethod

from typing_extensions import Sequence

from core.models import UserORM
from core.repository.abc_repository import AbstractRepository
from core.repository.sqlaclhemy_repository import SQLAlchemyAbstractRepository
from core.types.exceptions import NotFoundError


class UserAbstractRepository(AbstractRepository, ABC):
    @abstractmethod
    async def get(self, **kwargs) -> UserORM:
        raise NotImplementedError

    @abstractmethod
    async def create(self, **data) -> UserORM | None:
        raise NotImplementedError

    @abstractmethod
    async def update(self, user_id: int, **data) -> UserORM | None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, user_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    async def list(self, *args, **kwargs) -> Sequence[UserORM]:
        raise NotImplementedError


class UserSQLAlchemyRepository(UserAbstractRepository, SQLAlchemyAbstractRepository[UserORM]):
    async def get(self, user_id: int) -> UserORM:
        user: UserORM | None = await self._session.get(UserORM, user_id)

        if user is None:
            raise NotFoundError(f"User not found with given criteria")

        return user

    async def create(self, **data) -> UserORM | None:
        raise NotImplementedError

    async def update(self, user_id: int, **data) -> UserORM | None:
        user = await self.get(user_id=user_id)

        for key, value in data.items():
            if hasattr(user, key):
                setattr(user, key, value)

        await self._session.commit()
        await self._session.refresh(user)
        return user

    async def delete(self, model_id: int) -> None:
        raise NotImplementedError

    async def list(self, *args, **kwargs) -> Sequence[UserORM]:
        raise NotImplementedError
