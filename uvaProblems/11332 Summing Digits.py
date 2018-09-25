# Link: https://uva.onlinejudge.org/external/113/11332.pdf

from sys import stdin

# Method 1: String Manipulation
def printSum(line):
  while len(line) != 1:
    line = str(sum(map(int, list(line))))
  return line

# Method 2: Recursion + Integer Division
def printSumRec(num):
  # Base Case
  if num < 10:
    return num
  # Recursive case
  else:
    # Compute current line
    # and pass the remaining to the recursive call.
    sum = 0
    while num != 0:
      lastDigit = num % 10
      sum += lastDigit
      num //= 10
    return printSumRec(sum)

for line in stdin:
  line = line.strip()
  if line == '0':
    break
  print(printSumRec(int(line))) # printSum(line)
