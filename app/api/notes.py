from fastapi import APIRouter
from fastapi.params import Query
from fastapi import Depends
from typing import Annotated

from core.config import settings
from core.schemas.notes import (
    NoteReadSchema,
    NoteAddSchema,
    NoteShortSchema,
    NoteUpdateSchema,
    NoteFiltersSchema,
)
from core.schemas.users import UserReadSchema
from core.services.notes import NoteService

from .dependencies.auth.current_user import current_active_verify_user
from .dependencies.services.notes import get_note_service

router = APIRouter(
    prefix=settings.api.notes,
    tags=["Notes"]
)


@router.get(
    "/my",
    response_model=list[NoteShortSchema],
    summary="Get all user notes."
)
async def get_user_notes(
        service: Annotated[NoteService, Depends(get_note_service)],
        user: Annotated[UserReadSchema, Depends(current_active_verify_user)],
        filters: Annotated[NoteFiltersSchema, Query()],
):
    """
    Возвращает все заметки пользователя.
    """
    return await service.list(user_id=user.id, filters=filters)


@router.post("", response_model=NoteReadSchema)
async def add_note(
        note: NoteAddSchema,
        service: Annotated[NoteService, Depends(get_note_service)],
        user: Annotated[UserReadSchema, Depends(current_active_verify_user)],
):
    """
    Добавляет новую заметку и присваивает пользователю.
    """
    return await service.create(note=note, user_id=user.id)


@router.delete("/{note_id}", status_code=204)
async def delete_note(
        note_id: int,
        user: Annotated[UserReadSchema, Depends(current_active_verify_user)],
        service: Annotated[NoteService, Depends(get_note_service)],
):
    await service.delete(note_id=note_id, user_id=user.id)


@router.get("/{note_id}", response_model=NoteReadSchema)
async def get_note(
        note_id: int,
        user: Annotated[UserReadSchema, Depends(current_active_verify_user)],
        service: Annotated[NoteService, Depends(get_note_service)],
):
    return await service.get(note_id=note_id, user_id=user.id)


@router.patch("/{note_id}", response_model=NoteReadSchema)
async def update_note(
        note_id: int,
        note: NoteUpdateSchema,
        user: Annotated[UserReadSchema, Depends(current_active_verify_user)],
        service: Annotated[NoteService, Depends(get_note_service)],
):
    """
    Обновляет заметка пользователя и обрабатывает исключения, связанные с попыткой изменить
    чужую заметку и отсутствием заметки.
    """
    return await service.update(note_id=note_id, note_schema=note, user_id=user.id)


@router.get(
    "/{note_id}/add-in-favorite",
    status_code=204
)
async def add_in_favorite(
        user: Annotated[UserReadSchema, Depends(current_active_verify_user)],
        note_id: int,
        service: Annotated[NoteService, Depends(get_note_service)],
):
    await service.add_to_favorites(note_id=note_id, user_id=user.id)


@router.get(
    "/{note_id}/delete-from-favorites",
    status_code=204,
)
async def delete_from_favorites(
        service: Annotated[NoteService, Depends(get_note_service)],
        user: Annotated[UserReadSchema, Depends(current_active_verify_user)],
        note_id: int,
):
    await service.remove_from_favorites(note_id=note_id, user_id=user.id)
