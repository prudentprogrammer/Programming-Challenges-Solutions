#Link: https://uva.onlinejudge.org/external/3/336.pdf
import collections
from pprint import pprint


def bfs(G, initialNode, TTL):
  queue = collections.deque([(initialNode, TTL)])
  visited = set()
  while True:
    curNode, TTL = queue.popleft()
    if TTL ==



while True:
  testCases = int(input())
  if testCases == 0:
    break
  res = []
  G = collections.defaultdict(set)
  while True:
    currLine = [x for x in input().split() if x != '']
    for pair in [currLine[i:i+2] for i in range(0, len(currLine), 2)]:
      res.append(pair)
    #print(res)
    if res[-1] == ['0', '0']:
      break

  for node1, node2 in res[:testCases]:
    G[node1].add(node2)

  #pprint(G)
  for ind, query in enumerate(res[testCases:], 1):
    if query == ['0', '0']:
      break
    bfs(G.copy(), query[0], query[1])

  # print('Nodes: ', res[:testCases])
  # print('Queries: ', res[testCases:])

  break