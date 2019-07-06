while True:
  try:
    A, B = [int(x) for x in input().split()]
    print(A ^ B)
  except EOFError:
    break