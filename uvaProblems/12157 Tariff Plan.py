# Link: https://uva.onlinejudge.org/external/121/12157.pdf

for counter in range(1, int(input()) + 1):
  numberOfCalls = input()
  callDurations = [int(x) for x in input().split()]
  totalMiles = totalJuices = 0
  for call in callDurations:
    totalMiles += (call // 30) * 10 + 10
    totalJuices += (call // 60) * 15 + 15
  if totalMiles < totalJuices:
    print('Case {}: Mile {}'.format(counter, totalMiles))
  elif totalJuices < totalMiles:
    print('Case {}: Juice {}'.format(counter, totalJuices))
  else:
    print('Case {}: Mile Juice {}'.format(counter, totalMiles))