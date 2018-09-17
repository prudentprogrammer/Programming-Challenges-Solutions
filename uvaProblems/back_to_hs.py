# Link: https://uva.onlinejudge.org/external/100/10071.pdf

from sys import stdin

for line in stdin:
  v, t = map(float, input().split())
  print(int(2 * v * t))