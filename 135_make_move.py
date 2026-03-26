import random

# --- SETTINGS (From previous step) ---
BOARD_SIZE = 10
START_POS = (0, 0)
END_POS = (9, 9)
PENALTY = 2
FIXED_BAD_SQUARES = [(2, 3), (7, 5)] # Let's assume these were our random picks

def run_one_attempt():
    current_pos = START_POS
    path_taken = [START_POS]
    total_cost = 0
    steps = 0
    
    # The computer wanders until it hits the End square
    while current_pos != END_POS:
        # 1. Pick a random direction: Up, Down, Left, Right
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dr, dc = random.choice(moves)
        
        # 2. Calculate new potential position
        new_r = current_pos[0] + dr
        new_c = current_pos[1] + dc
        
        # 3. Check if move is inside the 10x10 board
        if 0 <= new_r < BOARD_SIZE and 0 <= new_c < BOARD_SIZE:
            current_pos = (new_r, new_c)
            path_taken.append(current_pos)
            
            # 4. Calculate cost
            step_cost = 1
            if current_pos in FIXED_BAD_SQUARES:
                step_cost += PENALTY
            
            total_cost += step_cost
            steps += 1
            
        # Safety break: stop if it's taking too long (e.g., 2000 steps)
        if steps > 2000:
            break
            
    return path_taken, total_cost

# Execute one trial
path, score = run_one_attempt()

print(f"Trial 1 Complete!")
print(f"Total Steps: {len(path)}")
print(f"Total Cost (including penalties): {score}")
print(f"Final Path: {path[:5]} ... {path[-5:]}") # Showing just start/end of path


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


# --- THE SEARCH LOOP ---
best_score = float('inf') # Start with "infinity" so the first find is always the best
best_path = []

print("Starting brute force search for the best path...")

for trial in range(1, 1001):
    path, score = run_one_attempt()
    
    # If this path is better than anything we've seen before...
    if score < best_score:
        best_score = score
        best_path = path
        print(f"Trial {trial}: New Record! Cost = {best_score}")
        display_path(best_path) # Uses your function to show the improvement

print(f"\nFinal Best Score after 1000 trials: {best_score}")
