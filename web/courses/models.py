from sqlalchemy import String, ForeignKey
from sqlalchemy import text as server_text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Course(Base):
    __tablename__ = 'course'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    is_life: Mapped[bool] = mapped_column(default=True, nullable=False)
    topics: Mapped[list["Topic"]] = relationship(back_populates="course")


class Topic(Base):
    __tablename__ = 'topic'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(2048), nullable=False)
    text: Mapped[str] = mapped_column(String(10_000), nullable=True)
    image_url: Mapped[str] = mapped_column(String(2048), nullable=True)
    time_learn: Mapped[int] = mapped_column(server_default=server_text('5'), nullable=False)
    cost: Mapped[int] = mapped_column(server_default=server_text('100'), nullable=False)
    course_id: Mapped[int] = mapped_column(ForeignKey('course.id'))
    course: Mapped["Course"] = relationship(back_populates='topics')
