while True:
  try:
    test_cases = int(input())
    numbers = sorted([input() for _ in range(test_cases)])
    for num in numbers:
      print(num)
  except EOFError:
    break