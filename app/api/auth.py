import fastapi_users.router
from fastapi import APIRouter

from .dependencies.auth.backend import auth_backend
from .dependencies.auth.fastapi_users import fastapi_users
from core.config import settings

router = APIRouter(
    prefix=settings.api.auth,
    tags=["Auth"],
)

router.include_router(
    router=fastapi_users.get_auth_router(auth_backend),
)
