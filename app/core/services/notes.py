from sqlalchemy import Sequence

from core.repository.notes import NoteRepository
from core.schemas.notes import NoteAddSchema, NoteReadSchema, NoteUpdateSchema, NoteFiltersSchema
from core.types.exceptions import NotFoundError, PermissionDeniedError


class NoteService:
    def __init__(self, repository: NoteRepository) -> None:
        self._repository: NoteRepository = repository

    async def list(self, user_id: int, filters: NoteFiltersSchema) -> Sequence[NoteReadSchema]:
        return await self._repository.list(
            user_id=user_id,
            order_by=filters.order_by,
            in_favorites=filters.in_favorites,
            is_desc=filters.desc,
        )

    async def create(self, note: NoteAddSchema, user_id: int) -> NoteReadSchema:
        return await self._repository.create(**note.model_dump(), user_id=user_id)

    async def update(self, note_schema: NoteUpdateSchema, note_id: int, user_id: int) -> NoteReadSchema:
        await self.get(note_id=note_id, user_id=user_id)
        return await self._repository.update(note_id=note_id, **note_schema.model_dump())

    async def delete(self, note_id: int, user_id: int) -> None:
        await self.get(note_id=note_id, user_id=user_id)
        await self._repository.delete(note_id=note_id)

    async def get(self, note_id: int, user_id: int) -> NoteReadSchema:
        note = await self._repository.get(note_id=note_id)
        if note is None:
            raise NotFoundError("Note not found")
        elif note.user_id != user_id:
            raise PermissionDeniedError("You don't have permission to view this note")
        return note

    async def add_to_favorites(self, note_id: int, user_id: int) -> None:
        await self.get(note_id=note_id, user_id=user_id)
        await self._repository.update(note_id=note_id, is_favorite=True)

    async def remove_from_favorites(self, note_id: int, user_id: int) -> None:
        await self.get(note_id=note_id, user_id=user_id)
        await self._repository.update(note_id=note_id, is_favorite=False)
