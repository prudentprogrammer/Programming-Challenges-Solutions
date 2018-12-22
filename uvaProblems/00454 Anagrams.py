import collections

anagramMap = None
res = [] # To remember the ordering in the original file

for _ in range(int(input())):
  currLine = input()
  if currLine == '':
    # Reset the map
    anagramMap = collections.defaultdict(list)

  allWords = ''.join(currLine.split(' '))
  res.append(currLine) # Store the words to remember the ordering
  anagramMap[''.join(sorted(allWords))].append(allWords)

for word in res:
  print(''.join(sorted(''.join(word.split(' ')))))
  print(anagramMap[''.join(sorted(''.join(word.split(' '))))])