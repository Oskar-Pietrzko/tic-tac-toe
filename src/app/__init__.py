from app.objects.board import print_board, get_empty_board, handle_move, is_win, is_playable
from app.objects.player import handle_player_interaction, change_player

import os


def main() -> None:
    running: bool = True
    board_size: int = 3
    board: list[list[str]] = get_empty_board(board_size)
    player: str = "X"

    while running:
        os.system("cls")

        print_board(board)

        move: tuple[int, int] = handle_player_interaction(player)
        board = handle_move(move[0], move[1], board, player)

        if is_win(board, player):
            running = False

            os.system("cls")
            print_board(board)
            print(f"Player {player} won!")
        elif not is_playable(board):
            running = False
            os.system("cls")
            print_board(board)
            print("Draw!")
        else:
            player = change_player(player)
