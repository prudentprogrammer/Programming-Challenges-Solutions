while True:
  try:
    curr_line = input()
    words = curr_line.split()
    replaced_words = {} 
    for word in words:
      if len(word) >= 4:
        if word[0:2] == word[2:4]:
          replaced_words[word] = word[2:]

    for k, v in replaced_words.items():
      curr_line = curr_line.replace(k, v)
    print(curr_line)

  except EOFError:
    break