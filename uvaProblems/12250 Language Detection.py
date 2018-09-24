# Link: https://uva.onlinejudge.org/external/122/12250.pdf

helloWords = {'HELLO': 'ENGLISH',
              'HOLA': 'SPANISH',
              'HALLO': 'GERMAN',
              'BONJOUR': 'FRENCH',
              'CIAO' : 'ITALIAN',
              'ZDRAVSTVUJTE': 'RUSSIAN'}
counter = 1
while True:
  currWord = input()
  if currWord == '#':
    break
  print('Case {}: {}'.format(counter, helloWords.get(currWord, 'UNKNOWN')))
  counter += 1