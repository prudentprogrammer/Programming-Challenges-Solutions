import sys

def simulate(grid, rows, cols, days):
    winning_life_form_map = {
        'R': 'P',
        'S': 'R',
        'P': 'S'
    }
    def get_winning_neighbor(grid, sq, i, j):
        winning_life_form = sq
        for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            nextX, nextY = dx + i, dy + j
            if 0 <= nextX < rows and 0 <= nextY < cols:
                if winning_life_form_map[sq] == grid[nextX][nextY]:
                    winning_life_form = winning_life_form_map[sq]
        return winning_life_form

    for dayNumber in range(days):
        updated_grid = []
        for i, row in enumerate(grid):
            updated_grid.append(''.join([get_winning_neighbor(grid, sq, i, j)
                                    for j, sq in enumerate(row)]))
        grid = updated_grid

    for row in grid:
        sys.stdout.write(row + "\n")

test_cases = int(sys.stdin.readline().strip())
for currentLine in range(test_cases):
    rows, cols, days = [int(x) for x in sys.stdin.readline().strip().split()]
    if rows == 0 and cols == 0:
        sys.stdin.readline().strip() # Ignore the empty row and input
    else:
        grid = [sys.stdin.readline().strip() for _ in range(rows)]
        simulate(grid, rows, cols, days)
    if currentLine != test_cases - 1:
        print()
