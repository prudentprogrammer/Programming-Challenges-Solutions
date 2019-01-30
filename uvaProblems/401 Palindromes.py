
mirrorMap = {
    'A' : 'A',
    'E' : '3',
    'H' : 'H',
    'I' : 'I',
    'J' : 'L',
    'L' : 'J',
    'M' : 'M',
    'O' : 'O',
    'S' : '2',
    'U' : 'U',
    'V' : 'V',
    'W' : 'W',
    'X' : 'X',
    'Y' : 'Y',
    'Z' : '5',
    '1' : '1',
    '2' : 'S',
    '3' : 'E',
    '5' : 'Z',
    '8' : '8'
}

def print_status(curr_line):
    is_palindrome = curr_line == curr_line[::-1]
    is_mirrored = False
    
    start, end = 0, len(curr_line) - 1
    while start <= end:
        mirrored_start_char = mirrorMap.get(curr_line[start], '')
        mirrored_end_char   = mirrorMap.get(curr_line[end], '')
        #print(mirrored_start_char, curr_line[start])
        if not (mirrored_start_char == curr_line[end] and mirrored_end_char == curr_line[start]):
            is_mirrored = False
        start += 1
        end -= 1
    
    if not is_palindrome and not is_mirrored: print('{} -- is not a palindrome.'.format(curr_line))
    elif is_palindrome and not is_mirrored: print('{} -- is a regular palindrome.'.format(curr_line))
    elif not is_palindrome and is_mirrored: print('{} -- is a mirrored string.'.format(curr_line))
    elif is_palindrome and is_mirrored: print('{} -- is a mirrored palindrome.'.format(curr_line))

while True:
    try:
        curr_line = input()
        print_status(curr_line)
    except EOFError:
        break # End of input


