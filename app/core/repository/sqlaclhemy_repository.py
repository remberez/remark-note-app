from typing import Type

from pydantic import BaseModel
from sqlalchemy import update, delete, select, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from abc_repository import AbstractRepository
from core.models import Base


# python version 3.12+
class SQLAlchemyRepository[
    ModelType: Base,
    CreateSchemaType: BaseModel,
    UpdateSchemaType: BaseModel,
](AbstractRepository):
    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self._session = session
        self.model = model

    async def get(self, **filters) -> ModelType:
        async with self._session as session:
            stmt = select(self.model).filter_by(**filters)
            result = await session.execute(stmt)
            return result.scalar_one()

    async def update(self, data: UpdateSchemaType, **filters) -> ModelType:
        async with self._session as session:
            stmt = update(self.model).filter_by(**filters).values(**data)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()

    async def delete(self, **filters) -> None:
        async with self._session as session:
            stmt = delete(self.model).filter_by(**filters)
            await session.execute(stmt)
            await session.commit()

    async def create(self, data: CreateSchemaType) -> ModelType:
        async with self._session as session:
            instance = self.model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def list(self, **filters) -> Sequence[ModelType]:
        async with self._session as session:
            stmt = select(self.model).filter_by(**filters)
            result = await session.execute(stmt)
            return result.scalars().all()
