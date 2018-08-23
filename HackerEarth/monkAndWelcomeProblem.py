# Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-welcome-problem/

def twoSum(a, b):
  for i, j in zip(a, b):
    print(i+j, end=' ')

size = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
twoSum(a, b)