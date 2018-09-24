# Link: https://uva.onlinejudge.org/external/124/12403.pdf

totalAmount = 0
for i in range(int(input())):
  currCommand = input()
  if currCommand == "report":
    print(totalAmount)
  else:
    totalAmount += int(currCommand.split()[-1])