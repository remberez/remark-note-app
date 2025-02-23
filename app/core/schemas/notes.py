from pydantic import BaseModel, Field, ConfigDict
from typing_extensions import Annotated


class NoteSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    title: Annotated[str, Field(max_length=25)]
    text: str


class NoteReadSchema(NoteSchema):
    id: int


class NoteAddSchema(NoteSchema):
    ...


class NoteShortSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    title: Annotated[str, Field(max_length=25)]
