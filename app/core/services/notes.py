from typing import Any

from sqlalchemy import Sequence, select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.notes import NoteORM
from core.schemas.notes import NoteAddSchema


class NoteService:
    @staticmethod
    async def get_notes(
            *,
            session: AsyncSession,
    ) -> Sequence[dict[str, Any]]:
        stmt = select(NoteORM.id, NoteORM.title).order_by(NoteORM.id)
        result = await session.execute(stmt)
        return [{"id": row.id, "title": row.title} for row in result]

    @staticmethod
    async def add_note(
            *,
            note: NoteAddSchema,
            user_id: int,
            session: AsyncSession,
    ) -> NoteORM:
        note = NoteORM(**note.model_dump(), user_id=user_id)
        session.add(note)
        await session.commit()
        return note

    @staticmethod
    async def delete_note(
            *,
            note_id: int,
            session: AsyncSession,
    ) -> None:
        stmt = select(NoteORM).filter_by(id=note_id)
        note = (await session.scalars(stmt)).first()

        if not note:
            raise ValueError("Not found")
        await session.delete(note)
        await session.commit()

    @staticmethod
    async def get_note(
            *,
            note_id,
            session: AsyncSession,
    ) -> NoteORM:
        stmt = select(NoteORM).filter_by(id=note_id)
        note = (await session.scalars(stmt)).first()

        if not note:
            raise ValueError("Not found")
        return note

    @staticmethod
    async def change_note(
            note_id: int,
            note_schema: NoteAddSchema,
            session: AsyncSession,
    ) -> NoteORM:
        stmt = select(NoteORM).filter_by(id=note_id)
        note = (await session.scalars(stmt)).first()

        if not note:
            raise ValueError("Not found")
        for key, value in note_schema.model_dump().items():
            setattr(note, key, value)
        await session.commit()
        return note

    @staticmethod
    async def get_user_notes(
            session: AsyncSession,
            user_id: int,
    ) -> Sequence[NoteORM]:
        stmt = select(NoteORM).filter_by(user_id=user_id)
        notes = await session.scalars(stmt)
        return notes.all()
