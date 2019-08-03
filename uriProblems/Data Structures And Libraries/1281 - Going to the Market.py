for _ in range(int(input())):
  sale_dict = {x[0]: float(x[1]) for x in [input().split() for _ in range(int(input()))]}
  total = sum([float(x[1]) * sale_dict[x[0]] for x in [input().split() for _ in range(int(input()))]])
  print('R$ {:.2f}'.format(total))