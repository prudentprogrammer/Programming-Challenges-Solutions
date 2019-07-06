A, B, C, D = [int(x) for x in input().split()]
condition = B > C and D > A and C + D > A + B and C > 0 and D > 0 and A % 2 == 0
print('{}'.format('Valores aceitos' if condition else 'Valores nao aceitos'))