for _ in range(int(input())):
  print(''.join([x for x in input() if x.islower()][::-1]))