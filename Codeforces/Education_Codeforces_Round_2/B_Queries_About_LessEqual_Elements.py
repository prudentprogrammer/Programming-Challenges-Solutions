import bisect

def less_than_or_equal(x, y):
    x.sort()
    queries = {}
    res = []
    for num in y:
        if num in queries:
            res.append(queries[num])
        else:
            ind = bisect.bisect(x, num)
            res.append(ind)
            queries[num] = ind
    
    #print(res)
    return ' '.join(str(x) for x in res)


_ = input()
x = [int(x) for x in input().split()]
y = [int(y) for y in input().split()]
print(less_than_or_equal(x, y))
