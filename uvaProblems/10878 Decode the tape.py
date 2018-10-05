# Link: https://uva.onlinejudge.org/external/108/10878.pdf

beginning = input()
holesMap = { 'o': 1, ' ': 0}
res = ''
while True:
  currLine = input()
  if currLine == beginning:
    break # End of tape, break
  res += chr(sum([2**(6 - ind) * holesMap[x] for ind, x in enumerate(currLine[2:6] + currLine[7:10])]))

print(res.rstrip())
