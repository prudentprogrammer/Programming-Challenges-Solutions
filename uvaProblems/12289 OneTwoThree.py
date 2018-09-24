# Link: https://uva.onlinejudge.org/external/122/12250.pdf

for _ in range(int(input())):
  currWord = input()
  if len(currWord) == 5:
    print(3)
  else:
    if currWord == 'one' or len(set('one') - set(currWord)) == 1:
      print(1)
    else:
      print(2)