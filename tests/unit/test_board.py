from app import Player
from app.board import Board


def test_board() -> None:
    board: Board = Board()

    expected_width: int = 3
    expected_height: int = 3
    expected_win_length: int = 3
    expected_board: list[list[str]] = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    assert board.width == expected_width
    assert board.height == expected_height
    assert board.win_length == expected_win_length
    assert board.board == expected_board

    ################################################

    board: Board = Board(4, 4, 2)

    expected_width: int = 4
    expected_height: int = 4
    expected_win_length: int = 2
    expected_board: list[list[str]] = [
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
        [" ", " ", " ", " "]
    ]

    assert board.width == expected_width
    assert board.height == expected_height
    assert board.win_length == expected_win_length
    assert board.board == expected_board

def test_move() -> None:
    board: Board = Board()
    player: Player = Player("X", board)

    board.move((0, 0), player)
    board.move((1, 0), player)
    board.move((2, 0), player)

    expected_board: list[list[str]] = [
        ["X", " ", " "],
        ["X", " ", " "],
        ["X", " ", " "]
    ]

    assert board.board == expected_board

def test_is_resolved() -> None:
    board: Board = Board()
    player: Player = Player("X", board)

    board.move((0, 0), player)
    board.move((0, 1), player)
    board.move((0, 2), player)

    board.move((1, 0), player)
    board.move((1, 1), player)
    board.move((1, 2), player)

    board.move((2, 0), player)
    board.move((2, 1), player)
    board.move((2, 2), player)

    expected_value: bool = True

    assert board.is_resolved() == expected_value

    ################################################

    board: Board = Board()
    player: Player = Player("X", board)

    board.move((0, 0), player)
    board.move((1, 0), player)
    board.move((2, 0), player)

    expected_value: bool = True

    assert board.is_resolved() == expected_value

def test_get_winner() -> None:
    board: Board = Board()
    player: Player = Player("X", board)

    board.move((0, 0), player)
    board.move((1, 0), player)
    board.move((2, 0), player)

    expected_winner: str = "X"

    assert board.get_winner() == expected_winner
