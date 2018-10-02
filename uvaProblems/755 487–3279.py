# Link: https://uva.onlinejudge.org/external/7/755.pdf

from string import ascii_uppercase
import collections

# Initialize the number pad here
allInputs = ascii_uppercase[:16] + ascii_uppercase[17:-1]
numbers = []
for i in range(2, 11):
  numbers.extend([i] * 3)
numberPad = { k: v for k, v in zip(allInputs, numbers) }

phoneMap = None
testCases = int(input())
for testCase in range(testCases):
  currLine = input()
  if currLine == '':
    # Reset phone Map
    phoneMap = collections.defaultdict(int)

  for _ in range(int(input())):
    curNum = ''
    for letter in input().replace('-', ''):
      curNum += str(numberPad.get(letter, letter))
    phoneMap[curNum] += 1

  sortedNums = sorted(((x, y) for x, y in phoneMap.items() if y > 1), key=lambda x: x[0])

  if len(sortedNums) == 0:
    print('No duplicates.')
  else:
    for (phoneNumber, count) in sortedNums:
      print('{}-{} {}'.format(phoneNumber[:3].strip(), phoneNumber[3:].strip(), count))

  if testCase != testCases - 1: # Don't print out new line on the last testcase
    print()