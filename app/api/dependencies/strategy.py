from fastapi.params import Depends
from fastapi_users.authentication.strategy import AccessTokenDatabase, DatabaseStrategy
from typing_extensions import Annotated

from core.config import settings
from core.models import AccessTokenORM


def get_database_strategy(
        access_token_db: Annotated[
            AccessTokenDatabase[AccessTokenORM],
            Depends(get_access_token_db),
        ]
) -> DatabaseStrategy:
    return DatabaseStrategy(
        access_token_db,
        lifetime_seconds=settings.auth.lifetime_seconds
    )
