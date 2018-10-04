# Link: https://uva.onlinejudge.org/external/4/444.pdf

from sys import stdin
from string import ascii_letters

allCharacters = ascii_letters + ' !,.;:?'

def handleEncryption(word):
  characterMap = { char: str(ord(char)) for char in allCharacters }
  return ''.join([ characterMap[letter] for letter in word ])[::-1]

def handleDecryption(numberString):
  characterMap = { str(ord(char)): char for char in allCharacters }
  i = 0
  res = ''
  while i < len(numberString):
    twoDigits = line[i:i + 2][::-1]
    threeDigits = line[i:i + 3][::-1]
    if twoDigits in characterMap:
      res += characterMap[twoDigits]
      i += 2
    elif threeDigits in characterMap:
      res += characterMap[threeDigits]
      i += 3
  return res[::-1]

for line in stdin:
  line = line.strip()
  if line.isdigit():
    print(handleDecryption(line))
  else:
    print(handleEncryption(line))