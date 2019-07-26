# Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1168
leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for _ in range(int(input())):
  print('{} leds'.format(sum([leds[int(char)]for char in input()])))