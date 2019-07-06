# Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1022

for _ in range(int(input())):
  expression = input().split()
  N1, D1 = int(expression[0]), int(expression[2])
  N2, D2 = int(expression[4]), int(expression[6])
  if expression[3] == '+':
    print('{}/{}'.format(N1*D2 + N2*D1, D1*D2))
  elif expression[3] == '-':
    print()
  elif expression[3] == '*':
    print()
  elif expression[3] == '/':
    print()