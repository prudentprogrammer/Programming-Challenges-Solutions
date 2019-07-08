for _ in range(int(input())):
  languages = set([input() for _ in range(int(input()))])
  if len(languages) == 1:
    print(languages.pop())
  else:
    print('ingles')