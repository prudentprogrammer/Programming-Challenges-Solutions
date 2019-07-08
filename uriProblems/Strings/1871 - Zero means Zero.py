while True:
    A, B = [int(x) for x in input().split()]
    if [A, B] == [0, 0]:
        break
    print(str(A + B).replace('0', ''))
