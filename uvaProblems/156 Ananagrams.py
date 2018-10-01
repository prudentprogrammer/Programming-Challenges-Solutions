# Link: https://uva.onlinejudge.org/external/1/156.pdf
import collections
import pprint
anagramMap = collections.defaultdict(list)
res = [] # To remember the ordering in the original file

while True:
  currLine = input()
  if currLine == '#':
    break # EOF
  else:
    allWords = [x for x in currLine.split() if x != '']
    res.extend(allWords)
    for word in allWords:
      curWord = ''.join(sorted(word.lower()))
      res.append(curWord)
      anagramMap[curWord].append(word)

for word in res:
  if len(anagramMap[word]) == 1:
    print(anagramMap[word])

