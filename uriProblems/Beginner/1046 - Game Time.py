start, end = [int(x) for x in input().split()]
hours = 0
if end > start:
  hours = (end - start)
else:
  hours = (end + 24) - start  
print('O JOGO DUROU {} HORA(S)'.format(hours))