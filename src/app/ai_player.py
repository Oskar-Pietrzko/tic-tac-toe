from app.difficulty import Difficulty
from app.player import Player
from app.board import Board

import random


class AIPlayer(Player):
    def __init__(self, symbol: str, board: Board, difficulty: Difficulty = Difficulty.HARD):
        Player.__init__(self, symbol, board)

        self._difficulty: Difficulty = difficulty

    def input_move(self) -> tuple[int, ...]:
        if self._difficulty == Difficulty.HARD:
            return self._find_winning_move() or self._block_opponents() or self._choose_best_available()
        elif self._difficulty == Difficulty.EASY:
            return self._random_empty_spot()
        else:
            raise NotImplementedError()

    def _find_winning_move(self) -> tuple[int, ...] | None:
        return self._find_best_move(self.symbol)

    def _block_opponents(self) -> tuple[int, ...] | None:
        opponents = {cell for row in self._board.board for cell in row if cell not in {" ", self.symbol}}

        for opponent_symbol in opponents:
            move = self._find_best_move(opponent_symbol)

            if move:
                return move

        return None

    def _find_best_move(self, symbol: str) -> tuple[int, ...] | None:
        for x in range(self._board.height):
            for y in range(self._board.width):
                if self._board.board[x][y] == " ":
                    self._board.board[x][y] = symbol

                    if self._board.get_winner() == symbol:
                        self._board.board[x][y] = " "

                        return x, y

                    self._board.board[x][y] = " "

        return None

    def _choose_best_available(self) -> tuple[int, ...] | None:
        mid_x, mid_y = self._board.height // 2, self._board.width // 2

        if self._board.board[mid_x][mid_y] == " ":
            return mid_x, mid_y

        corners = [(0, 0), (0, self._board.width - 1), (self._board.height - 1, 0), (self._board.height - 1, self._board.width - 1)]
        random.shuffle(corners)

        for x, y in corners:
            if self._board.board[x][y] == " ":
                return x, y

        available_moves = [(x, y) for x in range(self._board.height) for y in range(self._board.width) if self._board.board[x][y] == " "]

        return random.choice(available_moves) if available_moves else (0, 0)

    def _random_empty_spot(self) -> tuple[int, ...]:
        empty_spots = [
            (x, y)
            for x in range(self._board.height)
            for y in range(self._board.width)
            if self._board.board[x][y] == " "
        ]

        return random.choice(empty_spots) if empty_spots else (0, 0)
