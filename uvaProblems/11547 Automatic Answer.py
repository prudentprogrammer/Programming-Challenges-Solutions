# Link: https://uva.onlinejudge.org/external/115/11547.pdf

for _ in range(int(input())):
  n = int(input())
  secretFunction = lambda x: (abs((63*x + 7492) * 5 - 498) // 10) % 10
  print(secretFunction(n))