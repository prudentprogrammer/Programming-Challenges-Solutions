from collections import Counter
import heapq

elements = input()
nums = list(map(int, input().split()))
k = int(input())
counter = Counter(nums)
heapq.heapify(nums)
while len(nums):
  smallest_element = heapq.heappop(nums)
  if counter[smallest_element] == k:
    print(smallest_element)
    break