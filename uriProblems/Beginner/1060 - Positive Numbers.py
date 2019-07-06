count = [float(input()) > 0 for _ in range(6)].count(True)
print('{} valores positivos'.format(count))