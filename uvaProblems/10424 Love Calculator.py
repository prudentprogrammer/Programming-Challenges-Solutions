# Link: https://uva.onlinejudge.org/external/104/10424.pdf
from string import ascii_lowercase

def getSum(name):

  while len(name) != 1:



while True:
  try:
    person1, person2 = input(), input()
    letterDict = { letter: ind for ind, letter in enumerate(ascii_lowercase, 1) }
    print(sum([letterDict.get(letter, 0) for letter in person1]))
    print(sum([letterDict.get(letter, 0) for letter in person2]))

  except EOFError:
    break


  