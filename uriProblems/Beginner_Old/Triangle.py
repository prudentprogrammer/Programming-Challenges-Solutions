A, B, C = [float(x) for x in input().split()]
if A + B > C and B + C > A and C + A > B:
  print('Perimetro = {:.1f}'.format(A + B + C))
else:
  print('Area = {:.1f}'.format( ((A + B) * C) / 2.0) )