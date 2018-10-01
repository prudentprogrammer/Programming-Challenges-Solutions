# Link: https://uva.onlinejudge.org/external/1/148.pdf
import collections

d = collections.defaultdict(int)
for word in ['WILLIAM', 'SHAKESPEARE']:
  for letter in word:
    d[letter] += 1

dictWords = ['SPEAK', 'RUSSIAN', 'AWHILE', 'NOW', 'REALISM']

def isWordInDict(word, wordDict):
  for letter in word:
    if letter not in wordDict:
      return False
  return True

newWords = [word for word in dictWords if isWordInDict(word, d)]

def printAnagrams(newWords, targetSentence):
  print(newWords)
  def dfs(start, sentenceSoFar):
    if start == len(newWords) - 1:
      print(sentenceSoFar + ' ' + newWords[start])
      return
    else:
      for i in range(start, len(newWords)):
        chosenWord = newWords[i]

        dfs(i + 1, sentenceSoFar + ' ' + chosenWord)

  dfs(0, '')

targetSentence = 'WILLIAMSHAKESPEARE'

printAnagrams(sorted(newWords), targetSentence)