import random

def create_crossword(words: list[str]) -> list[list[str]]:
    """
    Generates a 10x10 word search puzzle with the given words.

    Args:
        words: A list of words that should appear in the Word Search Puzzle.

    Returns:
        A 2D list (list of lists) of characters representing the puzzle.
    """
    grid_size = 10
    # Initialize a 10x10 grid with empty spaces
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    # Define directions for word placement: (row_change, col_change)
    # Horizontal: (0, 1) right, (0, -1) left
    # Vertical: (1, 0) down, (-1, 0) up
    # Diagonal: (1, 1) down-right, (1, -1) down-left, (-1, 1) up-right, (-1, -1) up-left
    directions = [
        (0, 1), (0, -1),   # Horizontal
        (1, 0), (-1, 0),   # Vertical
        (1, 1), (1, -1),   # Diagonal
        (-1, 1), (-1, -1)  # More Diagonals
    ]

    # Try to place each word
    for word in words:
        placed = False
        # Try multiple times to place the word
        for _ in range(100):  # Limit attempts to avoid infinite loops for unplaceable words
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)
            dr, dc = random.choice(directions) # Choose a random direction

            if can_place_word(grid, word, row, col, dr, dc, grid_size):
                place_word(grid, word, row, col, dr, dc)
                placed = True
                break # Word placed, move to next word
        
        if not placed:
            print(f"Warning: Could not place word '{word}' in the puzzle after multiple attempts.")

    # Fill remaining empty spaces with random letters
    for r in range(grid_size):
        for c in range(grid_size):
            if grid[r][c] == ' ':
                grid[r][c] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    return grid

def can_place_word(grid: list[list[str]], word: str, start_row: int, start_col: int, 
                   dr: int, dc: int, grid_size: int) -> bool:
    """
    Checks if a word can be placed at a given starting position and direction.
    """
    word_len = len(word)
    for i in range(word_len):
        current_row = start_row + i * dr
        current_col = start_col + i * dc

        # Check boundaries
        if not (0 <= current_row < grid_size and 0 <= current_col < grid_size):
            return False
        
        # Check for conflicts with existing letters
        # If the cell is not empty, the existing letter must match the word's letter
        if grid[current_row][current_col] != ' ' and grid[current_row][current_col] != word[i].upper():
            return False
    return True

def place_word(grid: list[list[str]], word: str, start_row: int, start_col: int, 
               dr: int, dc: int):
    """
    Places a word onto the grid at the specified position and direction.
    Assumes can_place_word has already confirmed it's possible.
    """
    word_len = len(word)
    for i in range(word_len):
        current_row = start_row + i * dr
        current_col = start_col + i * dc
        grid[current_row][current_col] = word[i].upper() # Store in uppercase

# --- Helper function for displaying the grid (for testing purposes) ---
def print_grid(grid: list[list[str]]):
    for row in grid:
        print(' '.join(row))

# --- Example Usage ---
if _name_ == "_main_":
    words_to_find = ["LEARNING", "SCIENCE", "FUN", "DATA", "PUZZLE", "CODE", "PYTHON", "AI", "GAME", "SEARCH"]
    
    puzzle = create_crossword(words_to_find)
    
    print("Generated Word Search Puzzle:")
    print_grid(puzzle)
    
    print("\nWords to find:")
    for word in words_to_find:
        print(f"- {word}")

    print("\nLet's try another set of words:")
    words_to_find_2 = ["HELLO", "WORLD", "COMPUTER", "PROGRAMMING", "ALGORITHM"]
    puzzle_2 = create_crossword(words_to_find_2)
    print_grid(puzzle_2)
    print("\nWords to find:")
    for word in words_to_find_2:
        print(f"- {word}")
