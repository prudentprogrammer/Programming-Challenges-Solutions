for _ in range(int(input())):
  words = [x.strip() for x in input().split() if len(x.strip()) > 0]
  print(''.join(word[0] for word in words))