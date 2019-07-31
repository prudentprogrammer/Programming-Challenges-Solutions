for _ in range(int(input())):
  A, B = input().split()
  print(['encaixa', 'nao encaixa'][A[-len(B):] != B])