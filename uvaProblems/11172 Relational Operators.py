# Problem: UVa 11172 - Relational Operators
# Link: https://uva.onlinejudge.org/external/111/11172.pdf

for _ in range(int(input())):
  x, y = map(int, input().split(' '))
  if x < y:
    print("<")
  elif x > y:
    print(">")
  else:
    print("=")