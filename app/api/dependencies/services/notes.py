from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Annotated

from core.models import db_helper
from core.repository.notes import NoteRepository, SQLAlchemyUserRepository
from core.services.notes import NoteService


def get_sqlalchemy_note_repository(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> SQLAlchemyUserRepository:
    """
    Зависимость для внедрения репозитория SQLAlchemy для работы с заметками.
    """
    return SQLAlchemyUserRepository(session=session)


def get_note_service(
        note_repository: Annotated[NoteRepository, Depends(get_sqlalchemy_note_repository)],
) -> NoteService:
    return NoteService(repository=note_repository)
