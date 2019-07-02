name = input().strip()
salary = float(input().strip())
sales = float(input().strip())

print('TOTAL = R$ {:.2f}'.format(salary + 0.15 * sales))