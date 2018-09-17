# Problem: UVa 11044 - Searching for Nessy
# Link: https://uva.onlinejudge.org/external/110/11044.pdf

total = int(input())
for _ in range(total):
  n, m = map(int, input().split())
  print((n // 3) * (m // 3))