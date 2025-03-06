import time

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.models import db_helper
from core.config import settings
from contextlib import asynccontextmanager
from api import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    db_helper.dispose()

main_app = FastAPI(
    lifespan=lifespan
)
main_app.include_router(
    router,
)

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors.allow_origins,
    allow_credentials=settings.cors.allow_credentials,
    allow_methods=settings.cors.allow_methods,
    allow_headers=settings.cors.allow_headers,
)

if __name__ == '__main__':
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )
