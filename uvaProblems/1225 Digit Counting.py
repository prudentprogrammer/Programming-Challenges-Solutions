# Link: https://uva.onlinejudge.org/external/12/1225.pdf
from collections import Counter

def get_digit_count(target):
    temp = ''
    for i in range(1, target+1):
        temp += str(i)
        
    counts = Counter(temp)
    return ' '.join(str(counts.get(str(digit), 0)) for digit in range(0, 10))

for _ in range(int(input())):
    print(get_digit_count(int(input())))
