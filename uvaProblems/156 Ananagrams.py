# Link: https://uva.onlinejudge.org/external/1/156.pdf
import collections
anagramMap = collections.defaultdict(list)
res = [] # To remember the ordering in the original file

while True:
  currLine = input()
  if currLine == '#':
    break # EOF
  else:
    allWords = [x for x in currLine.split() if x != '']
    res.extend(allWords) # Store the words to remember the ordering
    for word in allWords:
      curWord = ''.join(sorted(word.lower()))
      anagramMap[curWord].append(word)

for word in sorted(res):
  curWords = anagramMap[''.join(sorted(word.lower()))]
  if len(curWords) == 1:
    print(curWords[0])

