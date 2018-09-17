# Link: https://uva.onlinejudge.org/external/100/10055.pdf

from sys import stdin

for line in stdin:
  hashmat_soldiers, opponent_soldiers = map(int, input().split())
  print(abs(hashmat_soldiers - opponent_soldiers))