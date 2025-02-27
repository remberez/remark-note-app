from fastapi_users import FastAPIUsers

from api.dependencies.backend import auth_backend
from api.dependencies.user_manager import get_user_manager
from core.models import UserORM
from core.types.user_id import UserIDType

fastapi_users = FastAPIUsers[UserORM, UserIDType](
    get_user_manager,
    [auth_backend]
)
