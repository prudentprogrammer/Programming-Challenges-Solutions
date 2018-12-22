# Link: https://uva.onlinejudge.org/external/1/100.pdf

from sys import stdin

arrayMemo = [0] * 999999

def collatz(n):
  if arrayMemo[n] != 0:
    return arrayMemo[n]

  if n == 1:
    return 1
  else:
    cycleLength = 0
    if n % 2 != 0:
      cycleLength = 1 + collatz(3 * n + 1)
    else:
      cycleLength = 1 + collatz(n // 2)

    arrayMemo[n] = cycleLength
    return cycleLength


for line in ['99 9999']:
  start, end = [int(x) for x in line.split()]

  maxCycleLength = 0
  for n in range(min(start, end), max(start, end)+1):
    try:
      maxCycleLength = max(maxCycleLength, collatz(n))
    except:
      print('ERRRO ON ', n)

  print('{} {} {}'.format(start, end, maxCycleLength))
