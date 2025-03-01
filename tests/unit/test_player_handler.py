from app.player_handler import PlayerHandler
from app.player import Player
from app.board import Board


def test_player_handler() -> None:
    board: Board = Board()
    player1: Player = Player("X", board)
    player2: Player = Player("O", board)
    player_handler: PlayerHandler = PlayerHandler(player1, player2)

    expected_players: list[Player] = [player1, player2]

    assert player_handler.players == expected_players

def test_next_player() -> None:
    board: Board = Board()
    player1: Player = Player("X", board)
    player2: Player = Player("O", board)
    player_handler: PlayerHandler = PlayerHandler(player1, player2)

    player_test1: Player = player_handler.next_player()
    player_test2: Player = player_handler.next_player()

    expected_player1: Player = player1
    expected_player2: Player = player2

    assert player_test1 == expected_player1
    assert player_test2 == expected_player2
