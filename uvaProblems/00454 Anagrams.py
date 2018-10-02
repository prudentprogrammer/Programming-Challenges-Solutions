import collections
anagramMap = collections.defaultdict(list)
res = [] # To remember the ordering in the original file

for _ in range(int(input())):
  while True:
    currLine = input()
    if currLine == '#':
      break

    allWords = ''.join(currLine.split(' '))
    res.append(currLine) # Store the words to remember the ordering
    curWord = ''.join(sorted(allWords))
    anagramMap[curWord].append(allWords)

print(res)
# for word in sorted(res):
#   curWords = anagramMap[''.join(sorted(word.lower()))]
#   if len(curWords) == 1:
#     print(curWords[0])