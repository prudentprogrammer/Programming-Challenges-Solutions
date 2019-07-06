A, B, C = [int(x) for x in input().split()]
res = [A, B, C] # assumption C > A and C > B and B > A

if A > B:
  res = [B, A, C]

if B > A and B > C:
  if A > C:
    res = [C, A, B]
  else:
    res = [A, C, B]

if A > B and A > C:
  if C > B:
    res = [B, C, A]
  else:
    res = [C, B, A]

for num in res:
  print(num)
print()
for num in [A, B, C]:
  print(num)