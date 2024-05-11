from fastapi import APIRouter

from games.repo import GameRepo
from games.schemas import SGame

router = APIRouter(
    prefix="/games",
    tags=["Игры"]
)


@router.get("/all")
async def get_all_games() -> list[SGame]:
    games: list[SGame] = await GameRepo.find_all()
    return games


@router.get("/{game_id}")
async def get_game_by_id(game_id: int) -> SGame | None:
    game: SGame | None = await GameRepo.find_by_id(game_id)
    return game
