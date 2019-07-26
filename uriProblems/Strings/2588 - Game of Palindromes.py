from collections import Counter
while True:
  try:
    word = input()
    counts = Counter(word)
    
  except EOFError:
    break
