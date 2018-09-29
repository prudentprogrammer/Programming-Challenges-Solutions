# Link: https://uva.onlinejudge.org/external/103/10324.pdf

totalTestCases = 1
while True:
  try:
    currLine = input()
    if currLine == '\n':
      break

    queries = int(input())
    totalSum = 0
    print('Case {}:'.format(totalTestCases))
    for query in range(queries):
      i, j = [int(x) for x in input().split()]
      i, j = min(i, j), max(i, j)
      if (currLine[j] - currLine[i]) in [0, j - i + 1]:
          print('No')
          break
      else: # Using the quirky else syntax for python
        print('Yes')

    totalTestCases += 1

  except EOFError: # Don't know how many lines in advance
    break