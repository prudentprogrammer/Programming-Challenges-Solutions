# Link: https://uva.onlinejudge.org/external/15/1583.pdf

max_items = 100001
cache = [float('+inf')] * max_items
for num in range(1, max_items):
    total_sum = num + sum(map(int, list(str(num)))) # Don't do this, instead use int division instead!
    if total_sum < max_items:
        cache[total_sum] = min(cache[total_sum], num)

for _ in range(int(input())):
    curr_num = int(input())
    print(0 if curr_num >= max_items or cache[curr_num] == float('+inf') else cache[curr_num])
