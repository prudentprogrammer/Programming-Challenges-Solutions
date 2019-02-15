# Link: https://uva.onlinejudge.org/external/100/10082.pdf

rows = [
"`1234567890-=",
"QWERTYUIOP[]\\",
"ASDFGHJKL;'",
"ZXCVBNM,./"
]

# Construct the mapping
charMap = {}
for row in rows:
    for left, right in zip(row, row[1:]):
        charMap[right] = left

while True:
    try:
        currLine = input()
        print(''.join(charMap.get(char, char) for char in currLine))
        
    except EOFError:
        break # End of input, break
