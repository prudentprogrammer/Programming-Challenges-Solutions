# Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/memorise-me/
from collections import Counter
n = int(input())
nums = Counter(list(map(int, input().split())))
queries = int(input())

for _ in range(queries):
  guess = int(input())
  if guess in nums:
    print(nums[guess])
  else:
    print('NOT PRESENT')

