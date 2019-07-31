for _ in range(int(input())):
  password = input()
  prod = 1
  for w in password.lower():
    if w in 'aeios':
      prod *= 3
    else:
      prod *= 2
  print(prod)