# Link: https://uva.onlinejudge.org/external/105/10550.pdf

def getTotalDegrees(start, first, second, last):
  firstRotation =  (start - first + 40) % 40
  secondRotation =  (second - first + 40) % 40
  lastRotation = (second - last + 40) % 40
  fraction = 360 / 40 # 360 degrees / 40 calibrations
  return int(1080 + (firstRotation + secondRotation + lastRotation) * fraction)

while True:
  start, first, second, last = map(int, input().split())
  if start == first == second == last == 0:
    break
  print(getTotalDegrees(start, first, second, last))
