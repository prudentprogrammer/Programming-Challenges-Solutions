# Link: https://uva.onlinejudge.org/external/120/12015.pdf

import collections

for counter in range(1, int(input()) + 1):
  webpagesMap = collections.defaultdict(list)
  mostRelevantWebpage = 0

  for _ in range(10):
    webpage, relevance = input().split()
    relevance = int(relevance)
    webpagesMap[relevance].append(webpage)
    mostRelevantWebpage = max(mostRelevantWebpage, relevance)

  print('Case #{}:'.format(counter))
  for webpage in webpagesMap[mostRelevantWebpage]:
    print(webpage)
