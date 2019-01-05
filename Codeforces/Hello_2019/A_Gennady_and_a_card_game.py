import sys

table_card = sys.stdin.readline().strip()
your_cards = sys.stdin.readline().strip().split()

for current_card in your_cards:
    if current_card[0] == table_card[0] or current_card[1] == table_card[1]:
        sys.stdout.write("YES\n")
        break

else:
    sys.stdout.write("NO\n")
