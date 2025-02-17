def handle_player_interaction(player: str) -> tuple[int, int]:
    move: str = str(input(f"Player {player}: "))
    row, column = move.strip().split(" ")

    return int(row), int(column)

def change_player(player: str) -> str:
    return "X" if player == "O" else "O"
