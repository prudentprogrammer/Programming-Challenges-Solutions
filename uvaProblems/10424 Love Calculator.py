# Link: https://uva.onlinejudge.org/external/104/10424.pdf
from string import ascii_lowercase

def getSum(name):
  if name < 10:
    return name

  curSum = 0
  while name != 0:
    curSum += (name % 10)
    name //= 10
  return getSum(curSum)

while True:
  try:
    person1, person2 = input(), input()
    letterDict = { letter: ind for ind, letter in enumerate(ascii_lowercase, 1) }
    person1Sum = getSum(sum([letterDict.get(letter.lower(), 0) for letter in person1]))
    person2Sum = getSum(sum([letterDict.get(letter.lower(), 0) for letter in person2]))
    print('{:.2f} %'.format( (min(person1Sum, person2Sum) * 100.0)/ max(person1Sum, person2Sum)))

  except EOFError:
    break