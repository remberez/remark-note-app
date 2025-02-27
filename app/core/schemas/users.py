from fastapi_users import schemas

from core.types.user_id import UserIDType


class UserReadSchema(schemas.BaseUser[UserIDType]):
    ...


class UserCreateSchema(schemas.BaseUserCreate):
    ...


class UserUpdateSchema(schemas.BaseUserUpdate):
    ...
