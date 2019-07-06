A, B = int(input()), int(input())
A, B = sorted([A, B])
print([x for x in range(A+1, B)])
print(sum(x for x in range(A+1, B) if x % 2 != 0))