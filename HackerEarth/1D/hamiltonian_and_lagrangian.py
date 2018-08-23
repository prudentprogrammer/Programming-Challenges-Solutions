# Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/hamiltonian-and-lagrangian/

def printScoresGreaterThanRightSide(scores):
  for i in range(len(scores)):
    flag = True
    for j in range(i+1, len(scores)):
      if scores[i] < scores[j]:
        flag = False
        break
    
    if flag or i == len(scores) - 1:
      print(scores[i], end=" ")

totalStudents = int(input())
scores = list(map(int, input().split()))
printScoresGreaterThanRightSide(scores)

