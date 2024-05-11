from dao.base import BaseRepo
from games.models import Game


class GameRepo(BaseRepo):
    model = Game