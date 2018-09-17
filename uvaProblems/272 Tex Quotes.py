# Link: https://uva.onlinejudge.org/external/2/272.pdf

from sys import stdin

endQuote = False
brackets = ['``', "''"]
for line in stdin:
  for letter in line:
    if letter == '"':
      print(brackets[endQuote], end='')
      endQuote = 1 - endQuote
    else:
      print(letter, end='')
