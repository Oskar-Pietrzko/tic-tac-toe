from app.player import Player

from itertools import cycle


class PlayerHandler:
    def __init__(self, *players: Player) -> None:
        self._players: list[Player] = list(players)
        self._player_iterator: cycle[Player] = cycle(self._players)

    @property
    def players(self) -> list[Player]:
        return self._players

    def add_player(self, player: Player) -> None:
        self._players.append(player)
        self._player_iterator = cycle(self._players)

    def next_player(self) -> Player:
        return next(self._player_iterator)
