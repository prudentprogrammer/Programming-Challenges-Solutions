while True:
  try:
    line = input()
    first_italic = first_bold = True
    res = []
    for char in line:
      if char == '_':
        res.append('<i>' if first_italic else '</i>')
        first_italic = not first_italic
      elif char == '*':
        res.append('<b>' if first_bold else '</b>')
        first_bold = not first_bold
      else:
        res.append(char)
    print(''.join(res))

  except EOFError:
    break