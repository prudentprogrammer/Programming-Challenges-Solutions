total = 0
for _ in range(2):
    info = [float(x) for x in input().strip().split()][1:]
    total += (info[0] * info[1])

print('VALOR A PAGAR: R$ {:.2f}'.format(total))