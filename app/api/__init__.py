from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.security import HTTPBearer

from core.config import settings
from .notes import router as note_router
from .auth import router as auth_router
from .users import router as user_router

http_bearer = HTTPBearer(auto_error=False)
router = APIRouter(
    prefix=settings.api.prefix,
    dependencies=[Depends(http_bearer)],
)

router.include_router(note_router)
router.include_router(auth_router)
router.include_router(user_router)
