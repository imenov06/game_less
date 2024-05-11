from sqlalchemy import select
from sqlalchemy.orm import selectinload

from courses.models import Course, Topic
from dao.base import BaseRepo
from database import session_maker


class CourseRepo(BaseRepo):
    model = Course

    @staticmethod
    async def find_all_courses(**filter_by):
        async with session_maker() as session:
            query = (
                select(Course)
                .filter_by(**filter_by)
                .options(selectinload(Course.topics))
            )
            res = await session.execute(query)
            result = res.unique().scalars().all()

            return result

    @classmethod
    async def find_by_id_course(cls, model_id: int):
        async with (session_maker() as session):
            query = (
                select(cls.model).filter_by(id=model_id)
                .options(selectinload(Course.topics))
            )
            result = await session.execute(query)
            return result.scalar_one_or_none()


class TopicRepo(BaseRepo):
    model = Topic
