for I in range(0, 21, 2):
  for offset in [1, 2, 3]:
    if I % 10 != 0:
      print('I={:.1f} J={:.1f}'.format(I * 0.1, (I * 0.1)+offset))
    else:
      print('I={} J={}'.format(int(I * 0.1), int((I*0.1)+offset)))