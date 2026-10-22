import random

# 1. Set up board dimensions
BOARD_SIZE = 10
START_POS = (0, 0)
END_POS = (9, 9)

# 2. Define the Penalty
PENALTY_VALUE = 2

# 3. Generate 2 unique "bad squares" at random
# We make sure they aren't the Start or End squares
possible_squares = [
    (r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE)
    if (r, c) != START_POS and (r, c) != END_POS
]

bad_squares = random.sample(possible_squares, 2)

# 4. Display the board layout
print("--- Game Board Initialized ---")
print(f"Start: {START_POS}")
print(f"End: {END_POS}")
print(f"Bad Squares (Penalty +{PENALTY_VALUE}): {bad_squares}")
print("-" * 30)

# Visual representation for us humans
for r in range(BOARD_SIZE):
    row_display = ""
    for c in range(BOARD_SIZE):
        if (r, c) == START_POS:
            row_display += " S "
        elif (r, c) == END_POS:
            row_display += " E "
        elif (r, c) in bad_squares:
            row_display += " X "  # X marks the bad squares
        else:
            row_display += " . "
    print(row_display)

 # Path
def display_path(path_taken):
    """
    Renders a 10x10 grid showing the specific route 
    the computer traveled.
    """
    # Create a blank 10x10 grid
    grid = [[" . " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    # 1. Place the path markers
    for (r, c) in path_taken:
        grid[r][c] = " * "

    # 2. Place the Fixed Bad Squares (so we see if the path hit them)
    for (r, c) in FIXED_BAD_SQUARES:
        grid[r][c] = " X "

    # 3. Place Start and End (Overwrites path/bad squares for clarity)
    sr, sc = START_POS
    er, ec = END_POS
    grid[sr][sc] = " S "
    grid[er][ec] = " E "

    # 4. Print the board
    print("\n--- Visualizing the Path ---")
    for row in grid:
        print("".join(row))
    print("-" * 28)
    print(f"Path Length: {len(path_taken)} steps")
