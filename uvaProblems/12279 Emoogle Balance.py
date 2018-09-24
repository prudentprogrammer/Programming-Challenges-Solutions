# Link: https://uva.onlinejudge.org/external/122/12250.pdf

counter = 1
while True:
  currLine = int(input())
  if currLine == 0:
    break
  treats = [int(x) for x in input().split()]
  emosTreats = treats.count(0)
  print('Case {}: {}'.format(counter, len(treats) - 2 * emosTreats))
  counter += 1