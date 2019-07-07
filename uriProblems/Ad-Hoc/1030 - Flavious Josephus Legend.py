st = []
def josephus(N, K):
  if N == 1:
    return 1
  else:
    st.append((N - 1))
    return ((josephus(N - 1, K) + K - 1) % N) + 1

test_cases = int(input())
for i in range(1, test_cases+1):
  total, start = [int(x) for x in input().split()]
  print('Case {}: {}'.format(i, josephus(total, start)))