# Link: https://uva.onlinejudge.org/external/112/11292.pdf
import heapq

# Faster than the other version, but still TLE. Going to write a solution in Java instead.
def get_minimum_gold_coins(dragon_heads, knights):
    if len(dragon_heads) > len(knights): # There are more heads than knights, can't be saved!
        return -1
    
    heap_dragon, heap_knights = [], []
    
    [heapq.heappush(heap_dragon, dragon)  for dragon in dragon_heads]
    [heapq.heappush(heap_knights, knight) for knight in knights]
    
    res = 0
    while heap_knights:
        if not heap_dragon:
            break
        
        smallest_knight = heapq.heappop(heap_knights)
        if heapq.nsmallest(1, heap_dragon)[0] <= smallest_knight:
            res += smallest_knight
            heapq.heappop(heap_dragon)
    
    return res if not heap_dragon else -1

'''
Brute force: O(n * m)
Will TLE

def get_minimum_gold_coins(dragon_heads, knights):
    if len(dragon_heads) > len(knights): # There are more heads, can't be saved!
        return -1
    visited = [False] * len(knights)
    knights.sort()
    
    res = 0
    for dragon_head in dragon_heads:
        head_chopped = False
        for ind, knight in enumerate(knights):
            if knight >= dragon_head and not visited[ind]:
                visited[ind] = True
                res += knight
                head_chopped = True
                break
        if not head_chopped:
            return -1
        
    return res
'''

while True:
    currLine = input()
    if currLine == "0 0":
        break # End of file
    number_of_dragon_heads, number_of_knights = [int(x) for x in currLine.split()]
    
    dragon_heads = [int(input()) for _ in range(number_of_dragon_heads)]
    knights = [int(input()) for _ in range(number_of_knights)]
    res = get_minimum_gold_coins(dragon_heads, knights)
    if res == -1:
        print('Loowater is doomed!')
    else:
        print(res)
