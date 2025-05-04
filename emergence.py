import numpy as np
import matplotlib.pyplot as plt

# Rule 110 transition table:
# 000 -> 0, 001 -> 1, 010 -> 1, 011 -> 1, 100 -> 1, 101 -> 0, 110 -> 1, 111 -> 0
rule_110 = {
    (0, 0, 0): 0, (0, 0, 1): 1, (0, 1, 0): 1, (0, 1, 1): 1,
    (1, 0, 0): 1, (1, 0, 1): 0, (1, 1, 0): 1, (1, 1, 1): 0
}

def rule_110_step(row):
    """Performs one step of Rule 110 on a given row."""
    new_row = np.zeros_like(row)
    for i in range(1, len(row) - 1):
        new_row[i] = rule_110[(row[i-1], row[i], row[i+1])]
    return new_row

def generate_rule_110_grid(size, steps):
    """Generates a grid of Rule 110 evolution."""
    grid = np.zeros((steps, size), dtype=int)
    grid[0, size // 2] = 1  # Start with a single '1' in the middle
    for i in range(1, steps):
        grid[i] = rule_110_step(grid[i - 1])
    return grid

def track_diagonal_patterns(grid):
    """Tracks diagonal patterns in the grid."""
    diagonals = []
    rows, cols = grid.shape
    for d in range(-cols + 1, rows):  # Diagonals can range from negative offset to positive
        diagonal = []
        for r in range(rows):
            c = r + d
            if 0 <= c < cols:
                diagonal.append(grid[r, c])
        diagonals.append(diagonal)
    return diagonals

def plot_grid(grid, title="Rule 110 Evolution"):
    """Plots the grid."""
    plt.figure(figsize=(10, 5))
    plt.imshow(grid, cmap="binary", interpolation="nearest")
    plt.title(title)
    plt.axis('off')
    plt.show()

def plot_diagonal_patterns(diagonals):
    """Plots the diagonal patterns."""
    plt.figure(figsize=(10, 5))
    for i, diagonal in enumerate(diagonals):
        plt.plot(diagonal, label=f"Diagonal {i}")
    plt.title("Diagonal Patterns in Rule 110")
    plt.xlabel("Index")
    plt.ylabel("State")
    plt.legend()
    plt.show()

# Parameters
grid_size = 101  # Width of the grid
steps = 101      # Number of steps to simulate

# Generate the grid for Rule 110
grid = generate_rule_110_grid(grid_size, steps)

# Track diagonal patterns
diagonals = track_diagonal_patterns(grid)

# Plot the grid (Rule 110 Evolution)
plot_grid(grid, title="Rule 110 Evolution")

# Plot the diagonal patterns
plot_diagonal_patterns(diagonals)
