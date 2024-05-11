from sqlalchemy import select, desc

from dao.base import BaseRepo
from database import session_maker
from users.models import User


class UserRepo(BaseRepo):
    model = User

    @classmethod
    async def find_all_user_order_by_balance(cls, **filter_by):
        async with session_maker() as session:
            query = select(cls.model).filter_by(**filter_by).order_by(desc(cls.model.balance))
            result = await session.execute(query)
            return result.scalars().all()
