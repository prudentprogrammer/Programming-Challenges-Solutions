# Link: https://uva.onlinejudge.org/external/123/12372.pdf

for i in range(int(input())):
  l, w, h = map(int, input().split())
  print('Case {}: {}'.format(i+1, ['bad', 'good'][l <= 20 and w <= 20 and h <= 20]))