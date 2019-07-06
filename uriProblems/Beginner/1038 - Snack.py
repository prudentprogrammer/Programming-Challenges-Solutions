X, Y = [int(x) for x in input().split()]
items = [0, 4, 4.50, 5, 2, 1.50]
print('Total: R$ {:.2f}'.format(items[X] * Y))