from pydantic import BaseModel, Field
from typing_extensions import Annotated


class NoteSchema(BaseModel):
    title: Annotated[str, Field(max_length=25)]
    text: str


class NoteReadSchema(NoteSchema):
    id: str


class NoteAddSchema(NoteSchema):
    ...
