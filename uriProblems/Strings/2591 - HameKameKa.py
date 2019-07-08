for _ in range(int(input())):
  attack = input()
  firstCommand = True
  count1 = count2 = 0
  for letter in attack:
    if letter == 'a':
      if firstCommand:
        count1 += 1
      else:
        count2 += 1
    if letter == 'k':
      firstCommand = False
  print('k' + ('a' * count1 * count2))