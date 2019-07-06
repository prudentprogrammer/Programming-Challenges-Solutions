A, B, C, D = [float(x) for x in input().split()]
avg = (2*A + 3*B + 4*C + D) / 10
print('Media: {:.1f}'.format(avg))
if avg > 7:
  print('Aluno aprovado.')
elif 5.0 <= avg <= 6.9:
  print('Aluno em exame.')
  X = float(input())
  print('Nota do exame: {:.1f}'.format(X))
  avg = (avg + X) / 2.0
  if avg >= 5.0:
    print('Aluno aprovado.')
  elif avg <= 4.9:
    print('Aluno reprovado.')
  print('Media final: {:.1f}'.format(avg))
elif avg < 5:
  print('Aluno reprovado.')
