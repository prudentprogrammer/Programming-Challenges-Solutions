# Link: https://uva.onlinejudge.org/external/1/119.pdf

totalTestCases = 0
while True:
  try:
    N = int(input())
    names = input().split()
    friends = { name: 0 for name in names }

    for _ in range(N):
      currLine = input().split()
      giver, amount, totalReceivers, receivers = currLine[0], int(currLine[1]), int(currLine[2]), currLine[3:]

      if amount > 0 and totalReceivers > 0:
        for receiver in receivers:
          friends[receiver] += (amount // totalReceivers)
        friends[giver] += ( -amount + (amount % totalReceivers) )

    totalTestCases += 1
    if totalTestCases > 1:
      print()
    for name in names:
      print('{} {}'.format(name, friends[name]))

  except EOFError: # Don't know how many lines in advance
    break