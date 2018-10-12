# Link: https://uva.onlinejudge.org/external/4/417.pdf

from string import ascii_lowercase
from collections import deque
from sys import stdin

lettersMap = {}
# First, perform a BFS on the letters
# and preprocess them basically.
initial = deque([("", 0)])
ascii_value = 1

for i in range(1, 6): # For all the 5 levels
  qsize = len(initial)
  all_letters = []

  for _ in range(qsize):
    curWord, levelNumber = initial.popleft()

    for letter in ascii_lowercase:
      if len(curWord) > 0 and curWord[-1] < letter:
        lettersMap[curWord + letter] = ascii_value
        all_letters.append((curWord + letter, levelNumber + 1))
        ascii_value += 1

      elif curWord == "": # For first level
        lettersMap[letter] = ascii_value
        all_letters.append((letter, levelNumber + 1))
        ascii_value += 1

  initial.extend(all_letters)

for line in stdin:
  print(lettersMap.get(line.strip(), 0))

