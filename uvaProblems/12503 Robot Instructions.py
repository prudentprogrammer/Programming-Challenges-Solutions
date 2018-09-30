# Link: https://uva.onlinejudge.org/external/125/12503.pdf

for _ in range(int(input())):
  curX = 0
  history = {}
  referenceMap = { 'LEFT': -1, 'RIGHT': +1 }

  for commandNumber in range(1, int(input()) + 1):
    curInstruction = input()
    if curInstruction in referenceMap:
      curX += referenceMap[curInstruction] # Add the +1 or -1 respectively
      history[commandNumber] = referenceMap[curInstruction] # Store the offset +1/-1
    else:
      prevOffset = history[int(curInstruction.split()[-1])]
      curX += prevOffset
      history[commandNumber] = prevOffset

  print(curX)
  