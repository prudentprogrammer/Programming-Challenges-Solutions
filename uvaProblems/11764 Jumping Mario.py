# Link: https://uva.onlinejudge.org/external/117/11764.pdf

for counter in range(1, int(input()) + 1):
  total_walls = input()
  wall_heights = [int(x) for x in input().split()]
  high_walls = low_walls = 0
  for i in range(len(wall_heights) - 1):
    if wall_heights[i] < wall_heights[i + 1]:
      high_walls += 1
    elif wall_heights[i] > wall_heights[i + 1]:
      low_walls += 1
  print('Case {}: {} {}'.format(counter, high_walls, low_walls))