from sqlalchemy import select

from database import session_maker


class BaseRepo:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
