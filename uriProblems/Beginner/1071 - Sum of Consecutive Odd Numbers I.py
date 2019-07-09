A, B = sorted([int(input()), int(input())])
print(sum(x for x in range(A+1, B) if x % 2 != 0))