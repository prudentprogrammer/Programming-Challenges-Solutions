amount = int(input().strip())
print(amount)
for denom in [100, 50, 20, 10, 5, 2, 1]:
    count = int(amount / denom) # 76 / 50
    print('{} nota(s) de R$ {},00'.format(count, denom))
    if count > 0:
        amount = (amount % denom)