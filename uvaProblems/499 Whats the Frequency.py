# Link: https://uva.onlinejudge.org/external/4/499.pdf
from collections import Counter

def get_high_frequency_letters(curr_line):
    c = Counter(curr_line)
    max_count = max(c.values())
    return '{} {}'.format(''.join(sorted(k for k, v in c.items() if v == max_count)), max_count)

while True:
    try:
        curr_line = [x for x in input() if x.isalpha()]
        print(get_high_frequency_letters(curr_line))
        
    except EOFError:
        break # End of input
