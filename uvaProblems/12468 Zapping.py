# Link: https://uva.onlinejudge.org/external/124/12468.pdf

from sys import stdin

for line in stdin:
  start, end = [int(x) for x in line.split()]
  if start == end == -1:
    break

  print(min(abs(end - start), 100 - abs(end - start)))
  