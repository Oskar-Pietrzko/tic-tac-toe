from typing import TYPE_CHECKING, Optional

import os


if TYPE_CHECKING:
    from app.player import Player


class Board:
    def __init__(self, width: int = 3, height: int = 3, win_length: int = 3) -> None:
        self._width: int = width
        self._height: int = height
        self._win_length: int = win_length
        self._board: list[list[str]] = []

        self._init_board()

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def win_length(self) -> int:
        return self._win_length

    @property
    def board(self) -> list[list[str]]:
        return self._board

    @board.setter
    def board(self, value: list[list[str]]) -> None:
        self._board = value

    def display(self) -> None:
        os.system("cls")

        for row in self._board:
            for cell in row:
                print(cell, end=" | ")

            print()

    def move(self, move: tuple[int, ...], player: "Player") -> None:
        x, y = move

        self._board[x][y] = player.symbol

    def is_resolved(self) -> bool:
        if all(cell != " " for row in self._board for cell in row):
            return True

        if self.get_winner() is None:
            return False

        return True

    def has_winner(self) -> bool:
        return self.get_winner() is not None

    def get_winner(self) -> str | None:
        for x in range(self._height):
            for y in range(self._width):
                symbol = self._board[x][y]

                if symbol != " " and self._dfs(x, y, symbol):
                    return symbol

        if all(cell != " " for row in self._board for cell in row):
            return None

        return None

    def _init_board(self) -> None:
        for i in range(self._height):
            self._board.append([])

            for j in range(self._width):
                self._board[i].append(" ")

    def _dfs(self, x: int, y: int, symbol: str) -> bool:
        directions = [
            (1, 0),
            (0, 1),
            (1, 1),
            (1, -1)
        ]

        for dx, dy in directions:
            count = 1
            nx, ny = x + dx, y + dy

            while 0 <= nx < self._height and 0 <= ny < self._width and self._board[nx][ny] == symbol:
                count += 1

                if count == self._win_length:
                    return True

                nx += dx
                ny += dy

        return False
