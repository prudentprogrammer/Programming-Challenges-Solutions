from collections import Counter
from string import ascii_lowercase

for _ in range(int(input())):
    curr_line = input()
    curr_line = [x for x in curr_line if x.isalpha()]
    
    diff = Counter(ascii_lowercase) - Counter(curr_line)
    if len(diff) == 0:
        print('frase completa')
    elif len(diff) > 13:
        print('frase mal elaborada')
    else:
        print('frase quase completa')
