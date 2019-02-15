# Link: https://uva.onlinejudge.org/external/119/11995.pdf

import heapq
from collections import deque

def determine_data_structure(queries):
    st, q, pq = [], deque([]), []
    index_map = { 0: 'stack', 1: 'queue', 2: 'priority queue' }
    bool_array = [True] * 3

    for query in queries:
        command, data = [int(x) for x in query.split()]
        if command is 1: # Insert into data structure
            if bool_array[0]: st.append(data)
            if bool_array[1]: q.append(data)
            if bool_array[2]: heapq.heappush(pq, -data) # -data for a max heap in python
        else: # Removal from data structure
            if bool_array[0]:
                if not st or st[-1] != data:
                    bool_array[0] = False
                else:
                    st.pop()
                    
            if bool_array[1]:
                if not q or q[0] != data:
                    bool_array[1] = False
                else: 
                    q.popleft()

            if bool_array[2]:
                if not pq or -heapq.nsmallest(1, pq)[0] != data:
                    bool_array[2] = False
                else:
                    heapq.heappop(pq)

    if  sum(bool_array) == 0: return 'impossible'
    elif sum(bool_array) > 1: return 'not sure'
    for ind, elem in enumerate(bool_array):
        if elem:
            return index_map[ind]


while True:
    try:
        queries = [input() for _ in range(int(input()))]
        print(determine_data_structure(queries))
    except EOFError:
        break # End of file
