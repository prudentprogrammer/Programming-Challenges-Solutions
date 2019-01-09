# Link: https://uva.onlinejudge.org/external/111/11192.pdf

while True:
    currLine = input().split()
    if not currLine: continue # Skip empty line
    if currLine[0] == "0": # End of input
        break
    groups, s = int(currLine[0]), currLine[1]
    
    # Print groups of strings reversed
    strides = len(s) // groups
    print(''.join(s[i:i+strides][::-1] for i in range(0, len(s), strides)))
