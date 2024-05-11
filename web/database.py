from typing import Annotated

from sqlalchemy import Integer, text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column
from config import get_settings

engine = create_async_engine(url=get_settings().get_db_url(), echo=True)
session_maker = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass


