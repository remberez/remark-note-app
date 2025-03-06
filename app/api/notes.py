from fastapi import (
    APIRouter,
    HTTPException
)
from fastapi.params import (
    Depends, Query
)
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Annotated

from core.config import settings
from core.models import db_helper
from core.schemas.notes import (
    NoteReadSchema,
    NoteAddSchema,
    NoteShortSchema,
    NoteUpdateSchema,
    NoteFiltersSchema,
)
from core.schemas.users import UserReadSchema
from core.services.notes import NoteService
from core.types.exceptions import (
    NotFoundError,
    PermissionDeniedError,
)

from .dependencies.auth.current_user import current_active_verify_user

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
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter)
        ],
        user: Annotated[
            UserReadSchema,
            Depends(current_active_verify_user)
        ],
        filers: Annotated[
            NoteFiltersSchema,
            Query(),
        ]
):
    """
    Returns a list of all the user's notes by user ID.
    """

    return await NoteService.get_user_notes(
        session=session,
        user_id=user.id,
        order_by=filers.order_by,
        is_desc=filers.desc,
    )


@router.post("", response_model=NoteReadSchema)
async def add_note(
        note: NoteAddSchema,
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        user: Annotated[UserReadSchema, Depends(current_active_verify_user)],
):
    return await NoteService.add_note(note=note, session=session, user_id=user.id)


@router.delete("/{note_id}", status_code=204)
async def delete_note(
        note_id: int,
        user: Annotated[UserReadSchema, Depends(current_active_verify_user)],
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    try:
        await NoteService.delete_user_note(note_id=note_id, session=session, user_id=user.id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except PermissionDeniedError as e:
        raise HTTPException(status_code=403, detail=str(e))


@router.get("/{note_id}", response_model=NoteReadSchema)
async def get_note(
        note_id: int,
        user: Annotated[UserReadSchema, Depends(current_active_verify_user)],
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    try:
        return await NoteService.get_note(note_id=note_id, session=session, user_id=user.id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except PermissionDeniedError as e:
        raise HTTPException(status_code=403, detail=str(e))


@router.patch("/{note_id}", response_model=NoteReadSchema)
async def change_note(
        note_id: int,
        note: NoteUpdateSchema,
        user: Annotated[UserReadSchema, Depends(current_active_verify_user)],
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
):
    try:
        return await NoteService.change_note(
            note_id=note_id,
            note_schema=note,
            user_id=user.id,
            session=session,
        )
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except PermissionDeniedError as e:
        raise HTTPException(status_code=403, detail=str(e))


@router.get(
    "/{note_id}/add-in-favorite",
    status_code=204
)
async def add_in_favorite(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        user: Annotated[
            UserReadSchema,
            Depends(current_active_verify_user),
        ],
        note_id: int,
):
    try:
        await NoteService.add_to_favorite(
            user_id=user.id,
            note_id=note_id,
            session=session,
        )
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except PermissionDeniedError as e:
        raise HTTPException(status_code=403, detail=str(e))


@router.get(
    "/{note_id}/delete-from-favorites",
    status_code=204,
)
async def delete_from_favorites(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        user: Annotated[
            UserReadSchema,
            Depends(current_active_verify_user),
        ],
        note_id: int,
):
    try:
        await NoteService.delete_from_favorites(
            note_id=note_id,
            user_id=user.id,
            session=session,
        )
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except PermissionDeniedError as e:
        raise HTTPException(status_code=403, detail=str(e))
