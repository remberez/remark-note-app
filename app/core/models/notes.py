from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, IntegerIDMixin, DateCreatedUpdatedMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import UserORM


class NoteORM(Base, IntegerIDMixin, DateCreatedUpdatedMixin):
    __tablename__ = "notes"

    title: Mapped[str] = mapped_column(String(length=25))
    text: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="cascade"))

    user: Mapped["UserORM"] = relationship(back_populates="notes")
