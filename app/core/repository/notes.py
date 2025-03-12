from abc import (
    ABC, abstractmethod
)

from sqlalchemy import (
    select, delete, update, desc, asc
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


class SQLAlchemyNoteRepository(SQLAlchemyAbstractRepository[NoteORM], NoteRepository):
    async def create(self, **data) -> NoteORM:
        async with self._session as session:
            note = NoteORM(**data)
            session.add(note)
            await session.commit()
            await session.refresh(note)
            return note

    async def delete(self, note_id: int) -> None:
        async with self._session as session:
            await session.execute(delete(NoteORM).where(NoteORM.id == note_id))
            await session.commit()

    async def update(self, note_id: int, **data) -> NoteORM:
        async with self._session as session:
            result = await session.execute(
                update(NoteORM).where(NoteORM.id == note_id).values(**data).returning(NoteORM)
            )
            await session.commit()
            return result.scalar_one()

    async def list(self, user_id: int, order_by: str, in_favorites: bool, is_desc: bool) -> Sequence[NoteORM]:
        async with self._session as session:
            stmt = select(NoteORM).where(NoteORM.user_id == user_id)

            if in_favorites is not None:
                stmt = stmt.where(NoteORM.in_favorites == in_favorites)

            if order_by:
                if is_desc:
                    stmt = stmt.order_by(desc(getattr(NoteORM, order_by)))
                else:
                    stmt = stmt.order_by(asc(getattr(NoteORM, order_by)))

            result = await session.execute(stmt)
            return result.scalars().all()

    async def get(self, note_id: int) -> NoteORM:
        async with self._session as session:
            stmt = select(NoteORM).filter_by(id=note_id)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()

    async def find_by_title(self, title: str) -> Sequence[NoteORM]:
        async with self._session as session:
            stmt = select(NoteORM).where(NoteORM.title.like("%" + title + "%"))
            result = await session.execute(stmt)
            return result.scalars().all()
