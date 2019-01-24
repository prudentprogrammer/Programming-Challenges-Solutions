# Link: https://uva.onlinejudge.org/external/119/11956.pdf

def print_hex(cmd, case_number):
    index = 0
    mem = [0] * 100
    for ch in cmd:
        if   ch == '>': index = (index + 1) % 100
        elif ch == '<': index = (index - 1 + 100) % 100
        elif ch == '+': mem[index] = (mem[index] + 1) % 256
        elif ch == '-': mem[index] = (mem[index] - 1 + 256) % 256

    print('Case {}: '.format(case_number), end='')
    print(' '.join([ ('%02X' % x) for x in mem]))

for case in range(1, int(input()) + 1):
    try:
        cmd = input()
        print_hex(cmd, case)
    except EOFError:
        break
