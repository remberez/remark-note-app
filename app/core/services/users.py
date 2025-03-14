from datetime import datetime

from core.repository.users import UserAbstractRepository


class UserService:
    def __init__(self, repository: UserAbstractRepository):
        self._repository = repository

    async def get(self, user_id: int):
        return await self._repository.get(user_id=user_id)

    async def make_user_premium(self, user_id: int, date_end: datetime):
        user = await self.get(user_id)

        if user.premium_end_date is not None and datetime.now() > user.premium_end_date:
            raise ValueError("User is already premium")
        date_end = date_end.replace(tzinfo=None)
        await self._repository.update(user_id=user_id, premium_end_date=date_end)
