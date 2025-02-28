from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Annotated

from core.config import settings
from core.models import db_helper
from core.schemas.notes import NoteReadSchema, NoteAddSchema, NoteShortSchema
from core.schemas.users import UserReadSchema
from core.services.notes import NoteService

from .dependencies.auth.current_user import current_active_verify_user

router = APIRouter(
    prefix=settings.api.notes,
    tags=["Notes"]
)


@router.get("", response_model=list[NoteShortSchema])
async def get_notes(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    return await NoteService.get_notes(session=session)


@router.post("", response_model=NoteReadSchema)
async def add_note(
        note: NoteAddSchema,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        user: Annotated[UserReadSchema, Depends(current_active_verify_user)],
):
    return await NoteService.add_note(note=note, session=session, user_id=user.id)


@router.delete("/{note_id}")
async def delete_note(
        note_id: int,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    try:
        await NoteService.delete_note(note_id=note_id, session=session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/{note_id}", response_model=NoteReadSchema)
async def get_note(
        note_id: int,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    try:
        return await NoteService.get_note(note_id=note_id, session=session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.patch("/{note_id}", response_model=NoteReadSchema)
async def change_note(
        note_id: int,
        note: NoteAddSchema,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    try:
        return await NoteService.change_note(note_id=note_id, note_schema=note, session=session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
