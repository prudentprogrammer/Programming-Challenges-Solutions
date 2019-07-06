number = int(input())
start = number + 1 if number % 2 == 0 else number
for i in range(start, start + 12, 2):
  print(i)