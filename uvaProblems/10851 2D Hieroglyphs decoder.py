# Link: https://uva.onlinejudge.org/external/108/10851.pdf

testCases = int(input())
for counter in range(testCases):
  curMatrix = []
  matrixMap = { '/': 0, '\\': 1}
  # Process Matrix
  for i in range(10):
    if i == 0 or i == 9:
      _ = input()
    else:
      curMatrix.append([matrixMap[x] for x in input()][1:-1])

  res = ''

  for col in range(0, len(curMatrix[0])):
    curNum = 0
    for row in range(7, -1, -1):
      curNum += (2**row * curMatrix[row][col])
    res += chr(curNum)

  print(res)

  if counter != testCases - 1:
    _ = input() # Newline
