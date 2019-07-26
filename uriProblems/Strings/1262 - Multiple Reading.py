def get_count(trace, cc):
  count = temp = 0
  for char in trace:
    if char == 'R':
      if temp < cc:
        if temp == 0:
          count += 1
        temp += 1
      else: # temp == cc
        temp = 1 # Reset cc
        count += 1
    else: # if == 'W'
      count += 1
      temp = 0
  return count

# for trace, cc in [('RWWRRR', 3), ('RWWRRRR', 3), ('WWWWW', 5), ('RRRRRRRRRR', 4), ('RWRRWWRWRWRRRWWRRRRWRRWRRWRRRRRRRRRWRWRWRRRRWRRRRR', 4)]:
#   print(get_count(trace, cc))

while True:
  try:
    trace, cc = input(), int(input())
    print(get_count(trace, cc))
  except EOFError:
    break
