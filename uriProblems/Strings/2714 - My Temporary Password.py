for _ in range(int(input())):
  password = input()
  if password[0:2] == "RA" and len(password[2:]) == 18:
    print(int(password[2:]))
  else:
    print('INVALID DATA')