import os


NEIGHBOURS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1), # Skip (0,0) as it's the current position
    (1, -1),  (1, 0),  (1, 1)
]

def get_neighbouring_positions(x, y, rows, cols):
    """Get all valid neighbouring positions within grid bounds."""
    neighbours = []
    for dx, dy in NEIGHBOURS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            neighbours.append((nx, ny))
    return neighbours

def parse_grid(file_path):
    """Parse the input file into a grid (list of lists)."""
    grid = []
    with open(file_path, 'r') as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid

def count_adjacent_rolls(grid):
    """Count the number of adjacent rolls (marked by @ symbol) for each roll in the grid."""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    accessible_rolls = 0
    
    # Iterate through each cell in the grid
    for x in range(rows):
        for y in range(cols):
            adjacent_rolls = 0
            if grid[x][y] == '@':  # If the cell contains a roll
                for nx, ny in get_neighbouring_positions(x, y, rows, cols): # Check each neighbour
                    # Increment the count for the neighbouring cell
                    adjacent_rolls += grid[nx][ny] == '@' # 0 if not a roll, 1 if roll
                if adjacent_rolls < 4:
                    accessible_rolls += 1
    return accessible_rolls

def main():
    input_file = 'input.txt'
    input_path = os.path.join(os.path.dirname(__file__), input_file)
    grid = parse_grid(input_path)
    accessible_rolls_count = count_adjacent_rolls(grid)
    print(f'Number of accessible rolls: {accessible_rolls_count}')
    
if __name__ == '__main__':
    main()
    