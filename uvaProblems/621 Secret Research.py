# Link: https://uva.onlinejudge.org/external/6/621.pdf

for _ in range(int(input())):
  currLine = input()
  if currLine in ['1', '4', '78']:
    print('+')
  elif len(currLine) >= 3:
    if currLine[-2:] == '35':
      print('-')
    elif currLine[0] is '9' and currLine[-1] is '4':
      print('*')
    else:
      print('?')
