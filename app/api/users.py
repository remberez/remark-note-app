from fastapi import APIRouter

from core.schemas.users import UserReadSchema, UserUpdateSchema
from .dependencies.auth.fastapi_users import fastapi_users
from core.config import settings

router = APIRouter(
    prefix=settings.api.users,
    tags=["Users"],
)

router.include_router(
    router=fastapi_users.get_users_router(
        UserReadSchema,
        UserUpdateSchema
    ),
)
