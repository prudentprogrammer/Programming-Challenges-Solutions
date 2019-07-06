number = int(input().strip())
hours  = int(input().strip())
amount_per_hour = float(input().strip())

print('NUMBER = {}'.format(number))
print('SALARY = U$ {:.2f}'.format(amount_per_hour * hours))