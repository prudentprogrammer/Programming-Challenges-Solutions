# Construct a table representing powers of two
table = [1 << i for i in range(32)]

testCases = int(input())
for _ in range(testCases):
  upper_bound = int(input())
  temp_sum = 0

  for binary_number in table:
    if binary_number <= upper_bound:
      temp_sum += binary_number
    else:
      break

  print( upper_bound * (upper_bound + 1) // 2 - (2 * temp_sum) )
