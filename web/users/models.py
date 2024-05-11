from datetime import datetime
from typing import Annotated

from sqlalchemy import String, text
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import EmailStr

from database import Base

created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), nullable=False)]


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(256), nullable=False)
    lastname: Mapped[str] = mapped_column(String(256), nullable=False)
    role_in_company: Mapped[str] = mapped_column(String(256), nullable=False)
    email: Mapped[EmailStr] = mapped_column(String(256), nullable=False)
    password: Mapped[str] = mapped_column(String(2048), nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False, default=True)
    balance: Mapped[int] = mapped_column(nullable=False, default=0)
    date_created: Mapped[datetime]
    avatar_url: Mapped[str] = mapped_column(String(2048), nullable=True)
