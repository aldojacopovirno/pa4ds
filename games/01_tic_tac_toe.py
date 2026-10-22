# Assignment
# Create a two-player tic-tac-toe game on a 3-by-3 board. Players take turns
# entering a row and column from 1 to 3. Reject occupied squares, detect a
# complete row, column, or diagonal, and stop with either a winner or a draw
# after nine valid moves.
#
# Solution

# A move is counted only after the program confirms the square is empty.
def display_board(board: list[list[str]]) -> None:
    """Print the three rows of the board."""
    for row in board:
        print(" | ".join(row))


def get_coordinate(label: str) -> int:
    """Read a 1-to-3 coordinate and return its zero-based index."""
    while True:
        value = int(input(label))
        if 1 <= value <= 3:
            return value - 1
        print("Enter a number from 1 to 3.")


def has_winner(board: list[list[str]]) -> bool:
    """Check each row, column, and diagonal for a three-in-a-row."""
    for index in range(3):
        if board[index][0] == board[index][1] == board[index][2] != " ":
            return True
        if board[0][index] == board[1][index] == board[2][index] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False


board = [[" ", " ", " "] for _ in range(3)]
player = "X"
move_count = 0
display_board(board)

while True:
    print(f"Player {player}")
    row = get_coordinate("Row (1-3): ")
    column = get_coordinate("Column (1-3): ")

    if board[row][column] != " ":
        print("That position is already occupied.")
        continue

    board[row][column] = player
    move_count += 1
    display_board(board)

    if has_winner(board):
        print(f"Winner: {player}")
        break
    if move_count == 9:
        print("Draw.")
        break

    # Alternate the player after a valid move.
    player = "O" if player == "X" else "X"
