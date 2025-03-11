from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Annotated

from core.models import db_helper
from core.models.notes import NoteORM
from core.repository.sqlaclhemy_repository import SQLAlchemyRepository
from core.schemas.notes import NoteAddSchema, NoteUpdateSchema
from core.services.notes_service import NoteService


def get_sqlalchemy_note_repository(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> SQLAlchemyRepository[NoteORM, NoteAddSchema, NoteUpdateSchema]:
    return SQLAlchemyRepository[NoteORM, NoteAddSchema, NoteUpdateSchema](NoteORM, session)


def get_note_service(
        repository: Annotated[
            SQLAlchemyRepository[NoteORM, NoteAddSchema, NoteUpdateSchema],
            Depends(get_sqlalchemy_note_repository),
        ]
) -> NoteService:
    return NoteService(repository)
