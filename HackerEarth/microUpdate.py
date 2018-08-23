# Link:https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/micro-and-array-update/

def updateArrayTLE(nums, k):
  count = 0
  while True:
    lessThan = False
    for i in range(len(nums)):
      if nums[i] < k: # If any numbers is less than k, let it to True
        lessThan = True
      nums[i] += 1

    if not lessThan:
      break
    count += 1
  return count

def updateArray(nums, k):
  minValue = min(nums)
  times = max(0, k - minValue)
  return times
    
testCases = int(input())
for _ in range(testCases):
  n, k = map(int, input().split())
  nums = list(map(int, input().split()))
  print(updateArray(nums, k))
