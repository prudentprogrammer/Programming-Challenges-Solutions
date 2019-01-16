# Link: https://uva.onlinejudge.org/external/116/11661.pdf

def get_min_distance(highway):
    prev = 0
    minDistance = len(highway)
    for ind, space in enumerate(highway):
        if space == 'Z':
            return 0
        elif space in ['D', 'R']:
            if highway[prev] != '.' and space != highway[prev]:
                minDistance = min(minDistance, ind - prev)
            prev = ind
    
    return minDistance

while True:
    test_cases = input()
    if test_cases == "0":
        break
    highway = input()
    print(get_min_distance(highway))
