test_cases = int(input())
for _ in range(test_cases):
  L = int(input())
  temp_sum = 0
  for curr_line in range(L):
    curr_word = input().strip()
    for ind, letter in enumerate(curr_word):
      alpha_pos = ord(letter) - ord('A')
      temp_sum += alpha_pos + curr_line + ind
  print(temp_sum)