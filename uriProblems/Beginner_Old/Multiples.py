X, Y = [int(x) for x in input().split()]
print(['Nao sao Multiplos', 'Sao Multiplos'][X % Y == 0 or Y % X == 0])