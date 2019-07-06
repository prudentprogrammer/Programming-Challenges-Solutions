X, Y = [float(x) for x in input().split()]
outputs = ['Origem', 'Eixo Y', 'Eixo X', 'Q1', 'Q2', 'Q3', 'Q4']
outputIndex = [
  X == 0 and Y == 0, 
  X == 0 and Y != 0, 
  X != 0 and Y == 0, 
  X > 0 and Y > 0, 
  X < 0 and Y > 0,
  X < 0 and Y < 0,
  X > 0 and Y < 0
].index(True)
print(outputs[outputIndex])