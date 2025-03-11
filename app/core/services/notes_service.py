from sqlalchemy import Sequence

from core.models.notes import NoteORM
from core.repository.abc_repository import AbstractRepository
from core.services.base import BaseService


class NoteService(BaseService):
    Model = NoteORM

    def __init__(self, repository: AbstractRepository):
        super().__init__(repository)

    async def get_user_notes(
            self,
            user_id: int,
            order_by: str = None,
            desc: bool = False,
    ) -> Sequence[Model]:
        return await self.repository.list(
            user_id=user_id,
            order_by=order_by,
            desc=desc,
        )
