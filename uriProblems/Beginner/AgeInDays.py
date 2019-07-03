age = int(input())
names = ['ano(s)', 'mes(es)', 'dia(s)']
for ind, unit in enumerate([365, 30, 1]):
  count = int(age / unit)
  print('{} {}'.format(str(count), names[ind]))
  if count > 0:
    age = age % unit