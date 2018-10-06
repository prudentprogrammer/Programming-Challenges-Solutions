# Link: https://uva.onlinejudge.org/external/119/11991.pdf
import collections

while True:
  try:
    _, queries = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]

    indexMap = collections.defaultdict(list)

    for ind, num in enumerate(nums, 1):
      indexMap[num].append(ind)

    for _ in range(queries):
      k, num = [int(x) for x in input().split()]
      if k > len(indexMap[num]):
        print(0)
      else:
        print(indexMap[num][k-1])
  except EOFError:
    break