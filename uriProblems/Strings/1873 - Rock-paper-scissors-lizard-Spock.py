import pprint

winning_combinations = {
  ('lagarto', 'papel'): 0,
  ('lagarto', 'spock'): 0,
  ('papel', 'pedra'): 0,
  ('papel', 'spock'): 0,
  ('pedra', 'lagarto'): 0,
  ('pedra', 'tesoura'): 0,
  ('spock', 'pedra'): 0,
  ('spock', 'tesoura'): 0,
  ('tesoura', 'lagarto'): 0,
  ('tesoura', 'papel'): 0
 }

for _ in range(int(input())):
  A, B = input().split()
  if A == B:
    print('empate')
  else:
    if (A, B) in winning_combinations:
      print('rajesh')
    else:
      print('sheldon')