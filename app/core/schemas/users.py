from datetime import datetime

from fastapi_users import schemas

from core.types.user_id import UserIDType


class UserReadSchema(schemas.BaseUser[UserIDType]):
    premium_end_date: datetime | None


class UserCreateSchema(schemas.BaseUserCreate):
    ...


class UserUpdateSchema(schemas.BaseUserUpdate):
    ...
