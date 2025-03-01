from app.difficulty import Difficulty
from app.player_handler import PlayerHandler
from app.ai_player import AIPlayer
from app.player import Player
from app.board import Board


def main() -> None:
    board: Board = Board()

    player1: Player = Player("X", board)
    player2: Player = Player("O", board)
    player_handler: PlayerHandler = PlayerHandler(player1, player2)

    while True:
        player: Player = player_handler.next_player()

        board.display()
        move: tuple[int, ...] = player.input_move()
        board.move(move, player)

        if board.is_resolved():
            break

    board.display()

    if board.has_winner():
        winner: str = board.get_winner()

        print(f"Player {winner} wins!")
    else:
        print("Draft!")
