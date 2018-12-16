from math import atan2, pi

vectors = []
for i in range(int(input())):
  x, y = [int(x) for x in input().split()]
  vectors.append((atan2(y, x), i + 1))

vectors.sort()
min_diff = float('+inf')
first_ind = second_ind = -1
print(vectors)
# The key here is to compare the difference between ith
# and i + 1-th vector and take the minimum. We should also
# take the difference between the last vector and the very first one
# in the very end.
for i in range(len(vectors)):
  first_vector, second_vector = vectors[(i + 1) % len(vectors)] , vectors[i]
  diff = first_vector[0] - second_vector[0]
  print(diff)
  if diff < 0:
    diff += 2 * pi

  if diff < min_diff:
    min_diff = diff
    first_ind, second_ind = first_vector[1], second_vector[1] 

print('{} {}'.format(first_ind, second_ind))
