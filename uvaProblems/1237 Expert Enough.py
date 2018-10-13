# Link: https://uva.onlinejudge.org/external/12/1237.pdf

totalTestCases = int(input())
for testCases in range(totalTestCases):
  size_of_db = int(input())
  data = []
  for _ in range(size_of_db):
    currLine = input().split()
    make, low, high = currLine[0], int(currLine[1]), int(currLine[2])
    data.append((make, low, high))

  for _ in range(int(input())): # queries
    price = int(input())
    count = 0
    greaterThan2 = False
    currentMake = ''
    for m, l, h in data:
      if l <= price <= h:
        count += 1
        if count >= 2:
          print('UNDETERMINED')
          greaterThan2 = True
          break
        currentMake = m

    if count == 0 and not greaterThan2:
      print('UNDETERMINED')
    if count == 1:
      print(currentMake)

  if testCases != totalTestCases - 1:
    print()