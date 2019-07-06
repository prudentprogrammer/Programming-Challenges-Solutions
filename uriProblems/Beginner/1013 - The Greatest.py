A, B, C = [int(x) for x in input().strip().split()]
x = lambda A, B: int((A + B + abs(A - B)) / 2.0)
print('{} eh o maior'.format(x(x(A, B), C)))