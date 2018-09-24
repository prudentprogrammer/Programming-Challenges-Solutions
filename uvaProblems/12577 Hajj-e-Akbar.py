# Link: https://uva.onlinejudge.org/external/125/12577.pdf

counter = 1
while True:
  currLine = input()
  if currLine == '*': break
  print('Case {}: Hajj-e-{}'.format(counter, ['Asghar','Akbar'][currLine == 'Hajj']))
  counter += 1