# Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/breakup-app/

def topTwoMaxIndices(nums):
  firstMax, secondMax = 0, 0
  firstIndex, secondIndex = -1, -1
  for i in range(1, len(nums)):
    if nums[i] > firstMax:
      secondMax = firstMax
      firstMax = nums[i]
      firstIndex = i
    
    elif nums[i] > secondMax:
      secondMax = nums[i]
      secondIndex = i

  return (firstIndex, secondIndex)   


testCases = int(input())
totalWeightage = 0
daysArray = [0] * 31
for _ in range(testCases):
  currLine = input()
  numbers = [int(x) for x in currLine.split() if x.isdigit()]
  for number in numbers:
    daysArray[number] += 1
    if currLine.startswith('G'):
      daysArray[number] += 1 # Twice the weightage

  
first, second = topTwoMaxIndices(daysArray)
if daysArray[first]
  pas



