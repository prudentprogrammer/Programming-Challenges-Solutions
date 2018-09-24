# Link: https://uva.onlinejudge.org/external/117/11727.pdf

for i in range(int(input())):
  nums = map(int, input().split())
  print('Case {}: {}'.format(i+1, sorted(nums)[1]))