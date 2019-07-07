for _ in range(int(input())):
  A, B = input().split()
  res = ''
  for ind in range(min(len(A), len(B))):
    res += (A[ind] + B[ind])

  if ind < len(A) - 1:
    res += A[ind+1:]
  elif ind < len(B) - 1:
    res += B[ind+1:]
  print(res)