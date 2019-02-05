# Link: https://uva.onlinejudge.org/external/1/100.pdf

# Works but unfortunately TLE :(
# Please look at the Java solution instead.

def calculate(start, end):
    start, end = min(start, end), max(start, end)
    
    def compute_cycle(n):
        count = 1
        while n != 1:
            if n % 2 != 0:
                n = 3 * n + 1
            else:
                n = n // 2
            count += 1
        return count
    
    return max(compute_cycle(x) for x in range(start, end+1))

while True:
    try:
        start, end = [int(x) for x in input().split()]
        print('{} {} {}'.format(start, end, calculate(start, end)))
    except EOFError:
        break # End of input
