# Link: https://uva.onlinejudge.org/external/119/11942.pdf

print('Lumberjacks:')
for _ in range(int(input())):
  heights = [int(x) for x in input().split()]
  high = low = False
  for i in range(len(heights) - 1):
    if heights[i] < heights[i + 1]:
      high = True
    else:
      low = True
  print(["Ordered", "Unordered"][high and low])