import sys
from collections import Counter

def number_of_ways(books):
    n = len(books)
    c = Counter(books)
    return sum(v * (n - v) for _, v in c.items()) // 2
    
n, m = [int(x) for x in sys.stdin.readline().strip().split()]
books = [int(x) for x in sys.stdin.readline().strip().split()] 
sys.stdout.write("{}\n".format(number_of_ways(books)))
