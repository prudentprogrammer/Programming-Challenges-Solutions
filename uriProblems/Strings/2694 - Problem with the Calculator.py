def get_nums_from_word(word):
  curr_num = 0
  res = []
  for char in word:
    if char.isdigit():
      curr_num = curr_num * 10 + int(char)
    else:
      if curr_num != 0:
        res.append(curr_num)
      curr_num = 0

  if curr_num != 0:
    res.append(curr_num)
  return res
  
for _ in range(int(input())):
  word = input()
  print(sum(get_nums_from_word(word)))