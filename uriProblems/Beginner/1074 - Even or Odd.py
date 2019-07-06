test_cases = int(input())
for _ in range(test_cases):
  number = int(input())
  if number == 0:
    print('NULL')
  else:
    parity = ['ODD', 'EVEN'][number % 2 == 0]
    pos = ['NEGATIVE', 'POSITIVE'][number > 0]
    print('{} {}'.format(parity, pos))