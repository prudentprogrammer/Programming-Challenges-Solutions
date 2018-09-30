# Link: https://uva.onlinejudge.org/external/125/12554.pdf

happyBirthdayLine = 'Happy birthday to you Happy birthday to you Happy birthday to Rujia Happy birthday to you'.split()

names, timesSaid = [], []
testCases = int(input())
for _ in range(testCases):
  names.append(input())
  timesSaid.append(0)

nameIndex = 0
while True:
  for word in happyBirthdayLine:
    print('{}: {}'.format(names[nameIndex], word))
    timesSaid[nameIndex] += 1
    nameIndex = (nameIndex + 1) % len(names)

  if all(x >= 1 for x in timesSaid):
    break