# Link: https://uva.onlinejudge.org/external/101/10189.pdf

def print_revealed_grid(grid, rows, cols):
    deltas = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if [x, y] != [0, 0]]    
    for row in range(rows):
        curRow = []
        for col in range(cols):
            if grid[row][col] == '*':
                curRow.append('*')
            else: # explore the 8 directions
                count = 0
                for dx, dy in deltas:
                    nextX, nextY = dx + row, dy + col
                    if not (0 <= nextX < rows and 0 <= nextY < cols):
                        continue # Skip since it's out of bounds
                    elif grid[nextX][nextY] == '*':
                        count += 1
                curRow.append(str(count))
        print(curRow)
    print()


while True:
    rows, cols = [int(x) for x in input().split()]
    print(rows, cols)
    if [rows, cols] == [0, 0]:
        break # end of input
    grid = [input() for _ in range(rows)]
    print_revealed_grid(grid, rows, cols)
