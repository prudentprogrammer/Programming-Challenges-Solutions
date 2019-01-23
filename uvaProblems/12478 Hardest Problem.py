# Link: https://uva.onlinejudge.org/external/124/12478.pdf
from collections import Counter

# Easy solution: Accepted
# You just scan it by hand and print the answer.
# print('KABIR')

# REAL way ;)
# Programmer's don't cheat (especially when it comes to algorithms :D )

names = [ 'RAKIBUL', 'ANINDYA', 'MOSHIUR', 'SHIPLU',
          'KABIR', 'SUNNY', 'OBAIDA', 'WASI']
grid = [
'OBIDAIBKR', 
'RKAULHISP', 
'SADIYANNO', 
'HEISAWHIA', 
'IRAKIBULS', 
'MFBINTRNO',
'UTOYZIFAH',
'LEBSYNUNE',
'EMOTIONAL'
]
rows, cols = len(grid), len(grid[0])
lens = list(set(len(name) for name in names))

# Form two hashmaps / dictionaries.
sortedMap    = { ''.join(sorted(name)): name for name in names }
frequencyMap = { ''.join(sorted(name)): 0    for name in names }

# Scan horizontally by slicing and examining the grid
for group in lens:
    for row in grid:
        for i in range(cols - group + 1):
            curSlice = row[i:i+group]
            sortedSlice = ''.join(sorted(curSlice))
            if sortedSlice in frequencyMap:
                frequencyMap[sortedSlice] += 1
            
# Scan vertically now.
for group in lens:
    for col in range(cols):
        for curRow in range(rows - group + 1):
            curSlice = ''.join(grid[i][col] for i in range(curRow, curRow + group))
            sortedSlice = ''.join(sorted(curSlice))
            if sortedSlice in frequencyMap:
                frequencyMap[sortedSlice] += 1

for k, v in frequencyMap.items():
    if v == 2: # The name that occurs twice
        print(sortedMap[k]) # Get the name from the original key.
        break
