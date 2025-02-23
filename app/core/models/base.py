from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class IntegerIDMixin:
    id: Mapped[int] = mapped_column(primary_key=True)
