salary = float(input())
conditions = [
  0 <= salary <= 400, 
  400.01 <= salary <= 800,
  800.01 <= salary <= 1200,
  1200.01 <= salary <= 2000,
  salary >= 2000.01 ]
true_index = conditions.index(True)
percentages = [15, 12, 10, 7, 4]
new_salary = ((percentages[true_index] / 100.0) * salary) + salary

print('Novo salario: {:.2f}'.format(new_salary))
print('Reajuste ganho: {:.2f}'.format(new_salary - salary))
print('Em percentual: {} %'.format(percentages[true_index]))