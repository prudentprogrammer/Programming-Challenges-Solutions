def printNotes(amount, heading, units, denominations):
  firstTime = True
  for denom in denominations:
    count = int(amount / denom)
    if firstTime:
        print(heading)
        firstTime = False

    print('{} {} de R$ {:.2f}'.format(count, units, denom / 100.0 if heading == 'MOEDAS:' else denom))
    if count > 0:
        amount = (amount % denom)

  return amount

amount = input().strip().split('.')
dollarAmount, coinAmount = int(amount[0]), int(amount[1])
remaining = printNotes(dollarAmount, 'NOTAS:', 'nota(s)', [100, 50, 20, 10, 5, 2])
if remaining > 0:
  coinAmount = remaining * 100 + coinAmount
printNotes(coinAmount, 'MOEDAS:', 'moeda(s)', [100, 50, 25, 10, 5, 1])