def compute_sum(n):
  while len(n) > 1:
    n = str(sum([int(x) for x in n]))
  return int(sum([int(x) for x in n]))

for _ in range(int(input())):
  line = input()
  n = len(line)
  print(compute_sum([line[i] for i in range(0, n, 2)]) + compute_sum([line[j] for j in range(1, n, 2)]))