def print_spiral(n):
  matrix = [['O' for _ in range(n)]  for _ in range(n)]
  rows = cols = n
  centerX, centerY = rows//2, cols//2
  offsetRight = offsetTop = offsetLeft = offsetRight = 0
  matrix[centerX][centerY] = 'X'

  def print_matrix():
    for row in matrix:
      print(row)
    print('@')

  print_matrix()
  prevX, prevY = (centerX, centerY)
  while matrix[-1][-1] != 'X':
    for r in range(centerX, cols):
      matrix[prevX][prevY] = 'O'
      matrix[prevX][r] = 'X'
      print_matrix()
      prevX, prevY = (prevX, r)
    break



print_spiral(3)