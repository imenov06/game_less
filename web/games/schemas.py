from pydantic import BaseModel


class SGame(BaseModel):
    id: int
    title: str
    image_url: str | None

