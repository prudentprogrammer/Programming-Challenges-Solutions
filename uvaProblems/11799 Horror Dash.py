# Link: https://uva.onlinejudge.org/external/117/11799.pdf

for counter in range(1, int(input()) + 1):
  speeds = [int(x) for x in input().split()][1:]
  print('Case {}: {}'.format(counter, max(speeds)))