from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class SUser(BaseModel):
    id: int
    firstname: str
    lastname: str
    role_in_company: str
    email: EmailStr
    password: str
    is_active: bool
    balance: int
    date_created: datetime
    avatar_url: str | None


class SUserRating(BaseModel):
    id: int
    firstname: str
    lastname: str
    balance: int
