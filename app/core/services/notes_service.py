from core.repository.abc_repository import AbstractRepository
from core.services.base import BaseService


class NoteService(BaseService):
    def __init__(self, repository: AbstractRepository):
        super().__init__(repository)

