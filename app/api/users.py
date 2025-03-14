from datetime import datetime

from fastapi import APIRouter, Body
from fastapi import Depends
from starlette.exceptions import HTTPException
from typing_extensions import Annotated

from core.schemas.users import UserReadSchema, UserUpdateSchema
from core.services.users import UserService
from .dependencies.auth.current_user import current_active_verify_user
from .dependencies.auth.fastapi_users import fastapi_users
from core.config import settings
from .dependencies.services.users import get_user_service

router = APIRouter(
    prefix=settings.api.users,
    tags=["Users"],
)

router.include_router(
    router=fastapi_users.get_users_router(
        UserReadSchema,
        UserUpdateSchema,
    ),
)


@router.post("/activate-premium")
async def make_user_premium(
        date_end: Annotated[datetime, Body()],
        user: Annotated[UserReadSchema, Depends(current_active_verify_user)],
        service: Annotated[UserService, Depends(get_user_service)]
):
    try:
        return await service.make_user_premium(user_id=user.id, date_end=date_end)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
