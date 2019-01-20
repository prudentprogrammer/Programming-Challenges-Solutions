# Link: https://uva.onlinejudge.org/external/4/445.pdf

def print_maze(currLine):
    times = 0
    key = { 'b': ' ' }
    for char in currLine:
        if char.isdigit():
            times += int(char)
        elif char == '!':
            print() # New line
        else:
            print(times * key.get(char, char), end='')
            # Reset times
            times = 0
    print()

while True:
    try:
        currLine = input()
        print_maze(currLine)
    except EOFError:
        break # End of input, break
