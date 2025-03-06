import datetime
from typing import Literal

from pydantic import BaseModel, Field, ConfigDict
from typing_extensions import Annotated

from core.schemas.base import OrderByDateFields


class NoteSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    title: Annotated[str, Field(max_length=25)]
    text: str


class NoteReadSchema(NoteSchema):
    id: int
    created_at: datetime.datetime | None = None
    update_at: datetime.datetime | None = None


class NoteAddSchema(NoteSchema):
    ...


class NoteShortSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    title: Annotated[str, Field(max_length=25)]
    in_favorites: bool


class NoteUpdateSchema(BaseModel):
    title: Annotated[str | None, Field(max_length=25)] = None
    text: str | None = None


class NoteFiltersSchema(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    order_by: OrderByDateFields | Literal["id"] = Field(
        "id", description="Field defines the field to be sorted."
    )
    desc: bool = False
    in_favorites: bool | None = None
    search: str | None = None
