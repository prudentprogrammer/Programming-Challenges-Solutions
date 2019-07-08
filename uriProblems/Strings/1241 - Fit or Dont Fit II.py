for _ in range(int(input())):
  A, B = input().split()
  if len(A) > len(B) and A[-1] == B[-1]:
    print('encaixa')
  elif len(A) == len(B) and all(int(x) >= int(y) for x, y in zip(A, B)):
    print('encaixa')
  else:
    print('nao encaixa')