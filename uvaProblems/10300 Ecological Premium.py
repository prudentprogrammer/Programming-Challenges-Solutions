# Link: https://uva.onlinejudge.org/external/103/10300.pdf

for _ in range(int(input())):
  premium = 0
  for _ in range(int(input())):
    size, animals, envFriendliness = list(map(int, input().split()))
    premium += (size * envFriendliness)
  print(premium)