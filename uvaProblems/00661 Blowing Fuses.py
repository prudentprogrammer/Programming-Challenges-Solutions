# Link: https://uva.onlinejudge.org/external/6/661.pdf

total_fuses = 21

fuses = [0] * total_fuses
while True:
    curr_line = input()
    if curr_line == '0 0 0':
        break # End of input
    
    devices, ops, capacity = [int(x) for x in curr_line.split()]
    
    devices_capacity = [int(input()) for _ in range(devices)]
    for ind, capacity in enumerate(devices_capacity, 1):
        fuses[ind] = capacity

    for i in range(ops):
        curr_outlet = int(input())
        if not fuses[curr_outlet]: # Then toggle it
            fuses[curr_outlet] 
