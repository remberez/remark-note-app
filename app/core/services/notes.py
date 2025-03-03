from typing import Literal

from sqlalchemy import Sequence, select, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.models.notes import NoteORM
from core.schemas.notes import NoteAddSchema, NoteUpdateSchema
from core.types.exceptions import NotFoundError, PermissionDeniedError


class NoteService:
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
    async def get_note(
            *,
            note_id: int,
            user_id: int,
            session: AsyncSession,
    ) -> NoteORM:
        stmt = select(NoteORM).options(joinedload(NoteORM.user)).filter_by(id=note_id)
        note: NoteORM = (await session.scalars(stmt)).first()

        if not note:
            raise NotFoundError("Not found.")

        if note.user.id != user_id:
            raise PermissionDeniedError("You do not have permission to delete this note.")

        return note

    @staticmethod
    async def change_note(
            note_id: int,
            note_schema: NoteUpdateSchema,
            user_id: int,
            session: AsyncSession,
    ) -> NoteORM:
        note = await NoteService.get_note(
            note_id=note_id,
            user_id=user_id,
            session=session,
        )

        for key, value in note_schema.model_dump(exclude_none=True).items():
            setattr(note, key, value)
        await session.commit()
        return note

    @staticmethod
    async def get_user_notes(
            session: AsyncSession,
            user_id: int,
            order_by: str = None,
            is_desc: bool = False,
    ) -> Sequence[NoteORM]:
        stmt = select(NoteORM).filter_by(user_id=user_id)

        if is_desc and order_by:
            stmt = stmt.order_by(desc(getattr(NoteORM, order_by)))
        elif not is_desc and order_by:
            stmt = stmt.order_by(order_by)

        notes = await session.scalars(stmt)
        return notes.all()

    @staticmethod
    async def delete_user_note(
            *,
            session: AsyncSession,
            user_id: int,
            note_id: int,
    ) -> None:
        stmt = select(NoteORM).options(joinedload(NoteORM.user)).filter_by(id=note_id)
        note: NoteORM = (await session.scalars(stmt)).first()

        if not note:
            raise NotFoundError("Not found.")

        if note.user.id != user_id:
            raise PermissionDeniedError("You do not have permission to delete this note.")

        await session.delete(note)
        await session.commit()
