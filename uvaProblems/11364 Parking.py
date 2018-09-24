# Problem: UVa 11364 - Parking
# Link: https://uva.onlinejudge.org/external/113/11364.pdf

testCases = int(input())
for _ in range(testCases):
  stores = int(input())
  parkingSpots = list(map(int, input().split()))
  print( (max(parkingSpots) - min(parkingSpots)) * 2)