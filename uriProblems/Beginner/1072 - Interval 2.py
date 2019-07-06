test_cases = int(input())
count = 0
for _ in range(test_cases):
  if 10 <= int(input()) <= 20:
    count += 1

print('{} in'.format(count))
print('{} out'.format(test_cases - count))