# Assignment
# Create a two-player tic-tac-toe game on a 3-by-3 board. Players take turns
# entering a row and column from 1 to 3. Reject occupied squares, detect a
# complete row, column, or diagonal, and stop with either a winner or a draw
# after nine valid moves.
#
# Solution

# Represent the board as three rows, each containing three cell strings.
# A space means an empty cell; a played cell contains "X" or "O".
# The type hints describe the expected arguments and return values. Python
# does not use these hints to check their types while the game runs.
def display_board(board: list[list[str]]) -> None:
    """Print the three rows of the board."""
    # Visit one row at a time so each printed line matches one board row.
    for row in board:
        # join inserts the separator between the three cell strings, making
        # their boundaries visible without changing the stored board.
        print(" | ".join(row))


def get_coordinate(label: str) -> int:
    """Read a 1-to-3 coordinate and return its zero-based index."""
    # Keep asking until an entered integer lies in the allowed interval.
    # A successful return ends both this loop and the function call.
    while True:
        # input returns text; int converts it before the numeric comparison.
        # Text that cannot represent an integer raises ValueError here;
        # this loop only retries integers that are outside the allowed range.
        value = int(input(label))

        # Both comparisons must hold: the coordinate is at least 1 and at
        # most 3. Subtract one to translate the user's positions 1, 2, 3
        # into Python's list indices 0, 1, 2.
        if 1 <= value <= 3:
            return value - 1

        # An out-of-range integer reaches this message, then the loop starts
        # again with a fresh input instead of returning an invalid index.
        print("Enter a number from 1 to 3.")


def has_winner(board: list[list[str]]) -> bool:
    """Check each row, column, and diagonal for a three-in-a-row."""
    # range(3) supplies indices 0, 1, and 2. At each index, check the row
    # with that index and then the column with that index.
    for index in range(3):
        # Keep the row index fixed and compare its three columns. The chained
        # comparisons require all three cells to match and the last cell to
        # differ from a space, so three empty cells cannot count as a win.
        if board[index][0] == board[index][1] == board[index][2] != " ":
            return True

        # Keep the column index fixed and compare the cells across all rows.
        # Return immediately if they contain the same non-empty symbol.
        if board[0][index] == board[1][index] == board[2][index] != " ":
            return True

    # Once every row and column has failed, check the diagonal from the
    # top-left corner through the centre to the bottom-right corner.
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    # Check the other diagonal, from top-right to bottom-left. These diagonal
    # checks also exclude spaces so an unused diagonal cannot win.
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    # Reach False only after every possible winning line has been checked.
    return False


# The list comprehension creates a fresh three-cell row on each iteration.
# This keeps rows independent: changing one cell cannot also change a cell
# in another row. range(3) repeats the construction three times; _ is the
# loop variable, whose value we do not need to use.
board = [[" ", " ", " "] for _ in range(3)]

# X takes the first turn. Count only valid moves into empty cells; this count
# will tell us when all nine cells have been filled without a winner.
player = "X"
move_count = 0

# Show the empty board before asking for the first move.
display_board(board)

# Repeat turns until a win or draw reaches a break below.
while True:
    print(f"Player {player}")

    # The helper returns indices from 0 to 2, so both coordinates are valid
    # for indexing this board. It checks their range before we use them here.
    row = get_coordinate("Row (1-3): ")
    column = get_coordinate("Column (1-3): ")

    # A non-space cell already belongs to a player. continue starts this loop
    # again before changing the board, move count, or current player, giving
    # the same player another attempt without using up a move.
    if board[row][column] != " ":
        print("That position is already occupied.")
        continue

    # Only an empty cell reaches this point. Store the current symbol, count
    # this valid move once, and display the new state before checking its result.
    board[row][column] = player
    move_count += 1
    display_board(board)

    # Check for a win before checking for a draw: even the ninth valid move
    # may complete a winning line. break ends the game loop immediately.
    if has_winner(board):
        print(f"Winner: {player}")
        break

    # With nine valid moves every cell is occupied. If the win check did not
    # end the game, there is no winning line and no further move is possible.
    if move_count == 9:
        print("Draw.")
        break

    # A valid move that did not end the game passes the turn to the other
    # player. This conditional expression chooses "O" when player is "X",
    # and chooses "X" otherwise; invalid attempts never reach this line.
    player = "O" if player == "X" else "X"
