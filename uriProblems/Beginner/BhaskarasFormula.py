import math
a, b, c = [float(x) for x in input().split()]
denom = int(2 * a)
determinant = (b**2 - (4 * a * c))
if denom == 0 or determinant < 0:
  print('Impossivel calcular')
else:
  R1, R2 = (-b + math.sqrt(determinant)) / (2 * a), (-b - math.sqrt(determinant)) / (2 * a)
  print('R1 = %.5f' % R1)
  print('R2 = %.5f' % R2)