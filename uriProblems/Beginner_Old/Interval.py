num = float(input())
if num < 0 or num > 100:
  print('Fora de intervalo')

outputs = ['[0,25]', '(25,50]', '(50,75]', '(75,100]']
for ind, (a, b) in enumerate([[0, 25], [25.00001, 50], [50.00001, 75], [75.00001, 100]]):
  if a <= num <= b:
    print('Intervalo {}'.format(outputs[ind]))
    break