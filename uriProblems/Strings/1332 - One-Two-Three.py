# one, two, three
# tne
for _ in range(int(input())):
    number = input()
    if len(number) == 3:
        if number[0:2] == 'on' or number[1:] == 'ne' or number[0] + number[-1] == 'oe':
            print(1)
        else:
            print(2)
    else:
        print(3)
