# Link: https://uva.onlinejudge.org/external/15/1586.pdf

molar_map = {
    'C' : 12.01,
    'H' : 1.008,
    'O' : 16.00,
    'N' : 14.01
}

def get_molar_mass(compound):
    i = total = 0
    while i < len(compound):
        element, count = compound[i], 0
        i += 1
        while i < len(compound) and compound[i].isdigit():
            count = count * 10 + int(compound[i])
            i += 1
        
        if count == 0:
            count = 1
            
        total += count * molar_map[element]
    return total
    
for _ in range(int(input())):
    print('{:.3f}'.format(get_molar_mass(input())))
