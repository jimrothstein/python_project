import random

# --- SETTINGS ---
BOARD_SIZE = 10
START_POS = (0, 0)
END_POS = (9, 9)
PENALTY = 2
FIXED_BAD_SQUARES = [(2, 3), (7, 5)]

# --- THE MEMORY (The Score Card) ---
# A 10x10 grid initialized to zeros
score_card = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def get_best_move(current_pos):
    r, c = current_pos
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    valid_moves = []

    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < BOARD_SIZE and 0 <= nc < BOARD_SIZE:
            valid_moves.append((nr, nc))

    # 20% of the time, act randomly (Exploration)
    if random.random() < 0.20:
        return random.choice(valid_moves)

    # 80% of the time, pick the neighbor with the highest score (Exploitation)
    # If scores are tied (like at the start), it picks randomly among them
    best_move = max(valid_moves, key=lambda pos: score_card[pos[0]][pos[1]])
    return best_move

def run_learning_attempt():
    current_pos = START_POS
    path_taken = [START_POS]
    total_cost = 0
    
    while current_pos != END_POS:
        # Ask the Memory for the next step
        next_step = get_best_move(current_pos)
        
        current_pos = next_step
        path_taken.append(current_pos)
        
        # Calculate Cost
        total_cost += 1
        if current_pos in FIXED_BAD_SQUARES:
            total_cost += PENALTY
        
        if len(path_taken) > 1000: # Safety break
            return None, float('inf')
            
    # REINFORCEMENT: If we reached the end, "reward" the squares in the path
    for (r, c) in path_taken:
        score_card[r][c] += 1
        
    return path_taken, total_cost

# --- RUNNING THE TRIALS ---
best_overall_score = float('inf')

for trial in range(1, 1001):
    path, score = run_learning_attempt()
    
    if path and score < best_overall_score:
        best_overall_score = score
        print(f"Trial {trial}: Found a path with cost {score}!")
        if trial % 100 == 0 or trial == 1: # Show progress occasionally
             display_path(path)

print(f"Final Best Score with Memory: {best_overall_score}")
