from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Game(Base):
    __tablename__ = 'game'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(2048), nullable=False)
    image_url: Mapped[str] = mapped_column(String(2048), nullable=True)

