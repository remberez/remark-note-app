from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Annotated

from core.models import db_helper

from core.repository.users import UserSQLAlchemyRepository
from core.services.users import UserService


def get_user_sqlalchemy_repository(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> UserSQLAlchemyRepository:
    return UserSQLAlchemyRepository(session=session)


def get_user_service(
        repository: Annotated[UserSQLAlchemyRepository, Depends(get_user_sqlalchemy_repository)],
) -> UserService:
    return UserService(repository=repository)
