# Link: https://uva.onlinejudge.org/external/100/10010.pdf

def get_coords(curr_word, grid, rows, cols):
    deltas = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if [dx, dy] != [0, 0]]
    for row in range(rows):
        for col in range(cols):
            for dx, dy in deltas:
                curr_x, curr_y = row, col
                index = 0
                #print(curr_x, curr_y, index, curr_word)
                while grid[curr_x][curr_y] == curr_word[index]:
                    curr_x, curr_y = curr_x + dx, curr_y + dy
                    index += 1
                    if index == len(curr_word):
                        return '{} {}'.format(row + 1, col + 1)
                    if not (0 <= curr_x < rows and 0 <= curr_y < cols):
                        break
                    
total_test_cases = int(input())
for test_case in range(1, total_test_cases + 1):
    
    _ = input() # Skip blank line
    rows, cols = [int(x) for x in input().split()]
    grid = [input().lower() for _ in range(rows)]
    
    for _ in range(int(input())):
        curr_word = input().lower()
        print(get_coords(curr_word, grid, rows, cols))

    if test_case < total_test_cases:
        print() # Print a blank line.
        
