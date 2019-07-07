letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for _ in range(int(input())):
  word, shift = input(), int(input())
  print(''.join([letters[letters.index(letter) - shift] for letter in word]))