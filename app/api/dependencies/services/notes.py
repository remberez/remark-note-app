from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Annotated

from core.models import db_helper
from core.repository.notes import NoteRepository, SQLAlchemyNoteRepository
from core.repository.users import UserAbstractRepository
from core.services.notes import NoteService
from .users import get_user_sqlalchemy_repository


async def get_sqlalchemy_note_repository(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> SQLAlchemyNoteRepository:
    """
    Зависимость для внедрения репозитория SQLAlchemy для работы с заметками.
    """
    return SQLAlchemyNoteRepository(session=session)


async def get_note_service(
        note_repository: Annotated[NoteRepository, Depends(get_sqlalchemy_note_repository)],
        user_repository: Annotated[UserAbstractRepository, Depends(get_user_sqlalchemy_repository)],
) -> NoteService:
    return NoteService(repository=note_repository, user_repository=user_repository)
