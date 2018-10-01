# Link: https://uva.onlinejudge.org/external/1/195.pdf

def printPermutation(s):

  def dfs(initial, rest):
    if len(rest) == 0:
      print(initial)
      return

    for i in range(len(rest)):
      if rest[i] == rest[i + 1]:
        continue
      dfs(initial + rest[i], rest[:i] + rest[i+1:])

  dfs('', s)


for _ in range(int(input())):
  printPermutation(sorted(input()))