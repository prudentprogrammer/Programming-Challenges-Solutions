# Link: https://uva.onlinejudge.org/external/9/902.pdf
# NOTE: Passes test cases but runtime error on UvA judge. :(
# Please reference the Java Code as it is Accepted (AC).
from collections import Counter

def get_high_frequency_substring(N, curr_line):
    c = Counter()
    for i in range(0, (len(curr_line) + 1) - N):
        c[curr_line[i:i+N]] += 1
    return c.most_common(1)[0][0]

while True:
    try:
        N, curr_line = [x for x in input().split() if len(x) > 0]
        print(get_high_frequency_substring(int(N), curr_line))
    except EOFError:
        break # End of input
