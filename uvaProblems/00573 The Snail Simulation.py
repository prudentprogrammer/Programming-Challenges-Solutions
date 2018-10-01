# Link: https://uva.onlinejudge.org/external/5/573.pdf

from sys import stdin

for line in stdin:
  maxHeight, dayDistance, nightDistance, fatigueFactor = [int(x) for x in line.split()]
  if maxHeight == 0:
    break
  days = 1
  initialHeight = 0
  downDistance = (dayDistance * 100) / fatigueFactor

  while True:
    initialHeight += dayDistance
    if dayDistance > 0:
      dayDistance -= downDistance

    if initialHeight >  maxHeight:
      break

    initialHeight -= nightDistance
    if initialHeight < 0:
      break

    days += 1

  print(['success on day {}'.format(days),
         'failure on day {}'.format(days)][initialHeight < 0])







  