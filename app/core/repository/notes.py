from abc import (
    ABC, abstractmethod
)

from sqlalchemy import (
    select, delete, update, desc, asc, func
)
from typing_extensions import (
    TypeVar, Sequence
)

from .abc_repository import AbstractRepository
from .sqlaclhemy_repository import SQLAlchemyAbstractRepository
from core.models.notes import NoteORM

NoteModel = TypeVar("NoteModel")


class NoteRepository(AbstractRepository[NoteModel], ABC):
    @abstractmethod
    async def create(self, **data) -> NoteModel:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, note_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    async def update(self, note_id: int, **data) -> NoteModel:
        raise NotImplementedError

    @abstractmethod
    async def list(self, user_id: int, order_by: str, in_favorites: bool, is_desc: bool) -> Sequence[NoteModel]:
        raise NotImplementedError

    @abstractmethod
    async def get(self, note_id: int) -> NoteModel:
        raise NotImplementedError

    @abstractmethod
    async def find_by_title(self, title: str) -> Sequence[NoteModel]:
        raise NotImplementedError

    @abstractmethod
    async def user_note_counter(self, user_id: int) -> int:
        raise NotImplementedError


class SQLAlchemyNoteRepository(SQLAlchemyAbstractRepository[NoteORM], NoteRepository):
    async def create(self, **data) -> NoteORM:
        note = NoteORM(**data)
        self._session.add(note)
        await self._session.commit()
        await self._session.refresh(note)
        return note

    async def delete(self, note_id: int) -> None:
        await self._session.execute(delete(NoteORM).where(NoteORM.id == note_id))
        await self._session.commit()

    async def update(self, note_id: int, **data) -> NoteORM:
        result = await self._session.execute(
            update(NoteORM).where(NoteORM.id == note_id).values(**data).returning(NoteORM)
        )
        await self._session.commit()
        return result.scalar_one()

    async def list(self, user_id: int, order_by: str, in_favorites: bool, is_desc: bool) -> Sequence[NoteORM]:
        stmt = select(NoteORM).where(NoteORM.user_id == user_id)

        if in_favorites is not None:
            stmt = stmt.where(NoteORM.in_favorites == in_favorites)

        if order_by:
            if is_desc:
                stmt = stmt.order_by(desc(getattr(NoteORM, order_by)))
            else:
                stmt = stmt.order_by(asc(getattr(NoteORM, order_by)))

        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def get(self, note_id: int) -> NoteORM:
        stmt = select(NoteORM).filter_by(id=note_id)
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def find_by_title(self, title: str) -> Sequence[NoteORM]:
        stmt = select(NoteORM).where(NoteORM.title.like("%" + title + "%"))
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def user_note_counter(self, user_id: int) -> int:
        stmt = select(func.count(NoteORM.id)).where(NoteORM.user_id == user_id)
        result = await self._session.execute(stmt)
        return result.scalar_one()
