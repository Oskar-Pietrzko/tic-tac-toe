from app.player import Player
from app.board import Board


def test_player() -> None:
    board: Board = Board()
    player: Player = Player("X", board)

    expected_symbol: str = "X"

    assert player.symbol == expected_symbol
