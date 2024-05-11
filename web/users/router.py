from fastapi import APIRouter
from users.repo import UserRepo
from users.schemas import SUser, SUserRating

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"]
)


@router.get("/all")
async def get_all() -> list[SUser]:
    users: list[SUser] = await UserRepo.find_all()
    return users


@router.get("/rating")
async def get_all_order_by_balance() -> list[SUserRating]:
    users: list[SUserRating] = await UserRepo.find_all_user_order_by_balance()
    return users


@router.get("/{user_id}")
async def get_all(user_id: int) -> SUser | None:
    user: SUser | None = await UserRepo.find_by_id(user_id)
    return user
