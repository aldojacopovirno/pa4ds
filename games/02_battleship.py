# Assignment
# Build a small Battleship game on a 3-by-4 grid. Place three ships at random so
# no two touch horizontally or vertically, but keep their locations hidden from
# the player. Read targets (e.g. `D3`), reject invalid or repeated shots, mark
# hits and misses, and stop when all ships have been found.
#
# Solution

# Import the random integer generator used to select ship positions. randint
# includes both bounds, so we must supply the final valid row and column indices.
from random import randint

# Keep the board dimensions and displayed column labels together. Uppercase
# names indicate settings we intend to keep fixed throughout the game.
ROWS = 3
COLUMNS = 4
COLUMN_LABELS = "ABCD"

# Store the hidden ships separately from the player's view. A dot means an
# empty hidden cell or an untried visible cell, depending on which grid we read.
# Each comprehension creates a fresh row list on every pass, so changing one
# cell affects only its own row. Each row begins with COLUMNS dots.
ships = [["."] * COLUMNS for _ in range(ROWS)]
visible_board = [["."] * COLUMNS for _ in range(ROWS)]

# During setup, count the ships successfully placed. After setup reaches three,
# this same counter will track how many ships the player still needs to hit.
ships_remaining = 0

# Try positions until three ships have been accepted. A rejected position
# starts another random attempt, so the number of attempts can vary.
while ships_remaining < 3:
    # Use zero-based indices: rows 0 through 2 and columns 0 through 3.
    row = randint(0, ROWS - 1)
    column = randint(0, COLUMNS - 1)

    # An existing ship already occupies this cell. continue skips the rest
    # of this attempt, keeping the ship count unchanged before drawing again.
    if ships[row][column] == "X":
        continue

    # Reset the flag for this candidate. The four offset pairs describe the
    # cells above, below, left, and right; diagonal neighbours are allowed.
    touches_ship = False
    for row_offset, column_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        # Unpack an offset pair and add it to the candidate's coordinates
        # to locate the neighbouring cell in that direction.
        neighbor_row = row + row_offset
        neighbor_column = column + column_offset

        # Both coordinates must lie inside the grid before we read the cell.
        # This also excludes negative indices, which Python would otherwise
        # interpret as positions counted from the far end of a list.
        if 0 <= neighbor_row < ROWS and 0 <= neighbor_column < COLUMNS:
            # Remember any neighbouring ship. Once True, the flag stays True
            # through the remaining neighbour checks for this candidate.
            if ships[neighbor_row][neighbor_column] == "X":
                touches_ship = True

    # Reject a cell touching a ship. An accepted cell is empty and has no
    # horizontal or vertical ship neighbour, so mark it and count it once.
    if touches_ship:
        continue
    ships[row][column] = "X"
    ships_remaining += 1

# Display only the visible grid so the ship positions stay hidden. join puts
# spaces between the column labels; enumerate numbers the rows from 1 for
# the player while leaving the stored row indices unchanged.
print("  " + " ".join(COLUMN_LABELS))
for row_index, row in enumerate(visible_board, start=1):
    print(row_index, " ".join(row))

# Count accepted, previously untried targets, including both hits and misses.
shots_taken = 0

# Setup left three ships to find. Keep asking until hits reduce this count to
# zero; a miss leaves the number of remaining ships unchanged.
while ships_remaining > 0:
    # Remove surrounding whitespace and normalize letters to uppercase so,
    # for example, " d3 " is read as "D3" before the format checks.
    target = input("Target (e.g. D3): ").strip().upper()

    # Reject a target if any requirement fails: exactly two characters, an
    # allowed column letter, and an allowed row digit. or stops at the first
    # True check, so a wrong length never reaches target[0] or target[1].
    if len(target) != 2 or target[0] not in COLUMN_LABELS or target[1] not in "123":
        print("Enter a coordinate (e.g. D3).")
        continue

    # Convert the validated labels to indices. index maps A-D to 0-3, and
    # subtracting one maps rows 1-3 to 0-2. For D3, column is 3 and row is 2.
    column = COLUMN_LABELS.index(target[0])
    row = int(target[1]) - 1

    # A visible X or o records an earlier shot. Ask again before counting or
    # checking the hidden grid, so the same ship cannot count as a new hit twice.
    if visible_board[row][column] != ".":
        print("You already fired there.")
        continue

    # Only a valid new target reaches this point. Count it once, then use the
    # hidden grid to decide which mark to put on the visible board.
    shots_taken += 1
    if ships[row][column] == "X":
        print("Hit!")
        visible_board[row][column] = "X"
        # A new hit finds one ship, moving the loop closer to its stopping point.
        ships_remaining -= 1
    else:
        print("Miss.")
        # Record the miss too, so future shots at this cell will be rejected.
        visible_board[row][column] = "o"

    # Redraw the updated visible board after each accepted shot. The hidden
    # ship grid is still kept separate, so unfound ships remain undisclosed.
    print("  " + " ".join(COLUMN_LABELS))
    for row_index, board_row in enumerate(visible_board, start=1):
        print(row_index, " ".join(board_row))

# Reaching this line means ships_remaining is zero. Report the total accepted
# shots used to find all three ships, including the misses along the way.
print(f"All ships found in {shots_taken} shots.")
