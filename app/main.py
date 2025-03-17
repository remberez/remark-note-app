import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from core.models import db_helper
from core.config import settings
from contextlib import asynccontextmanager
from api import router
from core.types.exceptions import PermissionDeniedError, NotFoundError


# LifeSpan handler for database connection and disposal
@asynccontextmanager
async def lifespan(_app: FastAPI):
    yield
    db_helper.dispose()

main_app = FastAPI(lifespan=lifespan)

# CORS Middleware
main_app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors.allow_origins,
    allow_credentials=settings.cors.allow_credentials,
    allow_methods=settings.cors.allow_methods,
    allow_headers=settings.cors.allow_headers,
)


# Handler for case when a user does not have permission to access an object
@main_app.exception_handler(PermissionDeniedError)
async def permission_denied_exception_handler(_request, exc):
    raise HTTPException(status_code=403, detail=str(exc))


# Handler for case when an object does not exist
@main_app.exception_handler(NotFoundError)
async def not_found_exception_handler(_request, exc):
    raise HTTPException(status_code=404, detail=str(exc))

# Main router
main_app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )
