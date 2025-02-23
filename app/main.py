import uvicorn
from fastapi import FastAPI

from app.core.models import db_helper
from core.config import settings
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    db_helper.dispose()

main_app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.reload,
    )
