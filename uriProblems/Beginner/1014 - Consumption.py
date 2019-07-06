info = [float(x) for _ in range(2) for x in input().strip().split()]
print('{:.3f} km/l'.format(info[0] / info[1]))