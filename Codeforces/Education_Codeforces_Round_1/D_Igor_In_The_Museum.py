import pprint

class Museum:
    def __init__(self, grid, rows, cols):
        self.grid = grid
        self.rows = rows
        self.cols = cols

        # Helper variables
        self.visited = set()
        self.islandsMap = {}
        self.result = []

        # Private helper functions
        self.__explore()

    # Private helper functions
    def __isValid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and (x, y) not in self.visited

    def __explore(self):
        islandNumber = 0
        def dfs(x, y):
            if not self.__isValid(x, y):
                return 0

            if self.grid[x][y] == '*':
                return 1

            self.visited.add((x, y))
            self.islandsMap[(x, y)] = islandNumber

            pictures = 0
            for nextX, nextY in [(x + 1, y), (x-1, y), (x, y+1), (x, y-1)]:
                pictures += dfs(nextX, nextY)
            return pictures

        # Perform dfs on entire grid to find groups of islands.
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == '.' and (i, j) not in self.visited:
                    self.result.append(dfs(i, j))
                    islandNumber += 1

    # Public function
    def get_number_of_paintings(self, startX, startY):
        return self.result[self.islandsMap[(startX, startY)]]




'''
def explore(grid, rows, cols):
  visited = set()
  islands = {}
  islandNumber = 0

  def dfs(x, y, islandNumber=0):
    if not (0 <= x < rows and 0 <= y < cols) or (x, y) in visited:
      return 0
    if grid[x][y] == '*':
      visited.add((x, y))
      islands[(x, y)] = islandNumber
      return 1
    
    visited.add((x, y))
    pics = 0
    for nextX, nextY in [(x + 1, y), (x - 1, y), (x, y+1), (x, y - 1)]:
      pics += dfs(nextX, nextY)
    result[x][y] = pics
    return pics

  for i in range(rows):
    for j in range(cols):
      if (i, j) not in visited and grid[i][j] == '.':
        result.append(dfs(i, j, islandNumber))
        islandNumber += 1

'''
rows, cols, queries = map(int, input().split())
grid = [input() for _ in range(rows)]
m = Museum(grid, rows, cols)

for _ in range(queries):
    start_x, start_y = map(int, input().split())
    start_x -= 1
    start_y -= 1
    print(m.get_number_of_paintings(start_x, start_y))








'''
class Solution:
  def __init__(self, grid, rows, cols):
    self.grid = grid
    self.rows = rows
    self.cols = cols
    
  def dfs(self, x, y, visited):
    if not (0 <= x < self.rows and 0 <= y < self.cols) or (x, y) in visited:
      return 0
            
    if grid[x][y] == '*':
      return 1
    
    visited.add((x, y))
    pictures = 0

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
      pictures += self.dfs(x + dx, y + dy, visited)
      
    return pictures

  def query(self, x, y):
    x -= 1
    y -= 1
    visited = set()
    print(self.dfs(x, y, visited))


if __name__ == '__main__':
  rows, cols, queries = [int(x) for x in input().split()]
  grid = []
  for _ in range(rows):
    grid.append(input())

  s = Solution(grid, rows, cols)
  for _ in range(queries):
    start, end = map(int, input().split())
    s.query(start, end)
'''  
