# Assignment
# Build a small Battleship game on a 3-by-4 grid. Place three ships at random so
# no two touch horizontally or vertically, but keep their locations hidden from
# the player. Read targets (e.g. `D3`), reject invalid or repeated shots, mark
# hits and misses, and stop when all ships have been found.
#
# Solution

from random import randint

# The visible board records shots while the separate ship grid stays hidden.
ROWS = 3
COLUMNS = 4
COLUMN_LABELS = "ABCD"

ships = [["."] * COLUMNS for _ in range(ROWS)]
visible_board = [["."] * COLUMNS for _ in range(ROWS)]
ships_remaining = 0

# Place three ships; only horizontal/vertical neighbors are forbidden.
while ships_remaining < 3:
    row = randint(0, ROWS - 1)
    column = randint(0, COLUMNS - 1)
    if ships[row][column] == "X":
        continue

    touches_ship = False
    for row_offset, column_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbor_row = row + row_offset
        neighbor_column = column + column_offset
        if 0 <= neighbor_row < ROWS and 0 <= neighbor_column < COLUMNS:
            if ships[neighbor_row][neighbor_column] == "X":
                touches_ship = True

    if touches_ship:
        continue
    ships[row][column] = "X"
    ships_remaining += 1

print("  " + " ".join(COLUMN_LABELS))
for row_index, row in enumerate(visible_board, start=1):
    print(row_index, " ".join(row))

shots_taken = 0
while ships_remaining > 0:
    target = input("Target (e.g. D3): ").strip().upper()
    if len(target) != 2 or target[0] not in COLUMN_LABELS or target[1] not in "123":
        print("Enter a coordinate (e.g. D3).")
        continue

    column = COLUMN_LABELS.index(target[0])
    row = int(target[1]) - 1
    if visible_board[row][column] != ".":
        print("You already fired there.")
        continue

    shots_taken += 1
    if ships[row][column] == "X":
        print("Hit!")
        visible_board[row][column] = "X"
        ships_remaining -= 1
    else:
        print("Miss.")
        visible_board[row][column] = "o"

    print("  " + " ".join(COLUMN_LABELS))
    for row_index, board_row in enumerate(visible_board, start=1):
        print(row_index, " ".join(board_row))

print(f"All ships found in {shots_taken} shots.")
