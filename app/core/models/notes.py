from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, IntegerIDMixin


class NoteORM(Base, IntegerIDMixin):
    __tablename__ = "notes"

    title: Mapped[str] = mapped_column(String(length=25))
    text: Mapped[str]
