def print_board(board: list[list[str]]) -> None:
    for column in board:
        for row in column:
            print(row, end=" | ")

        print()

def get_empty_board(board_size: int = 3) -> list[list[str]]:
    empty_board = []

    for i in range(board_size):
        empty_board.append([])

        for j in range(board_size):
            empty_board[i].append(" ")

    return empty_board

def handle_move(column: int, row: int, board: list[list[str]], player: str) -> list[list[str]]:
    if column > 3 or row > 3:
        raise ValueError("Invalid column or row")

    if board[row - 1][column - 1] == " ":
        board[row - 1][column - 1] = player

    return board

def is_win(board: list[list[str]], player: str) -> bool:
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    return False

def is_playable(board: list[list[str]]) -> bool:
    for column in board:
        for row in column:
            if row == " ":
                return True

    return False
