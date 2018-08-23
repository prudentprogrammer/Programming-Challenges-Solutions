# Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/range-query-2/

from enum import Enum

# Make it more readable using enums
class QueryEnum(Enum):
  EVENORODDQUERY = 0
  FLIPBITQUERY = 1

n, q = map(int, input().split())
bitArray = list(map(int, input().split()))

for _ in range(q):
  queryArray = list(map(int, input().split()))

  if queryArray[0] is QueryEnum.EVENORODDQUERY.value:
    l, r = queryArray[1] - 1, queryArray[2] - 1 # -1 since it is 1-based index
    
    if bitArray[r] == 1: # Just examine if the right most bit is set
      print('ODD')
    else:
      print('EVEN')
    
  if queryArray[0] is QueryEnum.FLIPBITQUERY.value:
    position = queryArray[1] - 1 # minus 1 since it is 1-based index
    bitArray[position] = 1 - bitArray[position]
