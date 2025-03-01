from app.board import Board


class Player:
    def __init__(self, symbol: str, board: Board) -> None:
        self._symbol: str = symbol
        self._board: Board = board

    @property
    def symbol(self) -> str:
        return self._symbol

    def input_move(self) -> tuple[int, int]:
        while True:
            user_input: str = input(f"Player {self._symbol}'s turn [x y]: ").strip()
            parts: list[str] = user_input.split()

            if len(parts) != 2:
                continue

            if not all(part.isdigit() for part in parts):
                continue

            x, y = tuple(map(lambda x: int(x) - 1, parts))

            if x < 0 or x >= self._board.width or y < 0 or y >= self._board.height:
                continue

            if self._board.board[x][y] != " ":
                continue

            return x, y

        raise Exception()
