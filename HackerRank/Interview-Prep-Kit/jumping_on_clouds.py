#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#
import collections
def __bfs(c):
    q = collections.deque([(0, 0)])
    while q:
        for _ in range(len(q)):
            curr, steps = q.popleft()
            if curr == len(c) - 1:
                return steps

            for step in [1, 2]:
                if 0 <= curr + step < len(c) and c[curr+step] == 0:
                    q.append((curr + step, steps + 1))
    return -1

def __greedy(c):
    steps = [0, 0]
    i = 0
    n = len(c)
    ans = 0
    while i < n - 1:
        taken = [False, False]
        if i + 1 < n and c[i + 1] == 0:
            steps[0] += 1
            taken[0] = True
        if i + 2 < n and c[i + 2] == 0:
            steps[1] += 1
            taken[1] = True
        i += (2 if taken[-1] else 1)
        ans += 1
    return ans

def jumpingOnClouds(c):
    # return __bfs(c)
    return __greedy(c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
