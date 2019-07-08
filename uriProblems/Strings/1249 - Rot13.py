from string import ascii_lowercase, ascii_uppercase
while True:
  try:
    word = input()
    res = ''
    for letter in word:
      if letter.isalpha():
        if letter.islower():
          res += ascii_lowercase[(ascii_lowercase.index(letter) + 13) % 26]
        elif letter.isupper():
          res += ascii_uppercase[(ascii_uppercase.index(letter) + 13) % 26]
      else:
        res += letter
    print(res)
  except EOFError:
    break