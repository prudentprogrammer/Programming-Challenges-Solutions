# Link: https://uva.onlinejudge.org/external/114/11498.pdf

while True:
  testCases = int(input())
  if testCases == 0:
    break

  divisionPoint = tuple(map(int, input().split()))
  for i in range(testCases):
    x, y = map(int, input().split())
    if x == divisionPoint[0] or y == divisionPoint[1]:
      print('divisa')

    elif y > divisionPoint[1]:
      if x < divisionPoint[0]:
        print('NO')
      else:
        print('NE')

    elif y < divisionPoint[1]:
      if x < divisionPoint[0]:
        print('SO')
      else:
        print('SE')
    
      

