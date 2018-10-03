# Link: https://uva.onlinejudge.org/external/2/245.pdf

def processWord(currWord, wordsSoFar):
  if currWord:
    print(currWord, end='')
    wordsSoFar.insert(0, currWord)
  return ''

def processNumber(currNum, wordsSoFar):
  if currNum:
    print(wordsSoFar[currNum - 1], end='')
    wordsSoFar.insert(0, wordsSoFar.pop(currNum - 1))
  return 0

res = []
while True:
  currLine = input()
  if currLine == '0':
    break
  i = curNum = 0
  curWord = ''

  for token in currLine:
    if token.isdigit():
      curNum = curNum * 10 + int(token)
    elif token.isalpha():
      curWord += token
    else:
      curWord = processWord(curWord, res)
      curNum = processNumber(curNum, res)
      print(token, end='')

  processWord(curWord, res)
  processNumber(curNum, res)
  print()