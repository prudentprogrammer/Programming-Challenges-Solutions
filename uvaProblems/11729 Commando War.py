# Link: https://uva.onlinejudge.org/external/117/11729.pdf

def get_minimum_time(soldiers):
    res = total_brief_times = 0
    for brief_time, execution_time in soldiers:
        total_brief_times += brief_time
        res = max(res, total_brief_times + execution_time)
    return res

counter = 1
while True:
    test_cases = input()
    if test_cases == "0":
        break
    soldiers = []
    
    for i in range(int(test_cases)):
        brief_time, execution_time = [int(x) for x in input().split()]
        soldiers.append((brief_time, execution_time))

    soldiers.sort(key=lambda x: -x[1]) # Sort by descending time of execution time.
    print('Case {}: {}'.format(counter, get_minimum_time(soldiers)))
    counter += 1
