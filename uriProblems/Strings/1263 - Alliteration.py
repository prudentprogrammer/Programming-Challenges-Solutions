while True:
  try:
    sentence = input()
    prev = count = 0
    in_group = False
    seen = '#'
    for word in sentence.split():
      first_letter = word[0].lower()
      if first_letter == seen:
        in_group = True
      else:
        seen = first_letter
        if in_group: 
          count += 1
          in_group = False
        
    count += in_group
    print(count)
  except EOFError:
    break