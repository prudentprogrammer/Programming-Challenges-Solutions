A, B, C = sorted([float(x) for x in input().split()], reverse = True)
if A >= B + C:
  print('NAO FORMA TRIANGULO')
else:
  if (A ** 2) == (B ** 2 + C ** 2):
    print('TRIANGULO RETANGULO')
  if (A ** 2) > (B ** 2 + C ** 2):
    print('TRIANGULO OBTUSANGULO')
  if (A ** 2) < (B ** 2 + C ** 2):
    print('TRIANGULO ACUTANGULO')
  if len(set([A, B, C])) == 1:
    print('TRIANGULO EQUILATERO')
  if len(set([A, B, C])) == 2:
    print('TRIANGULO ISOSCELES')