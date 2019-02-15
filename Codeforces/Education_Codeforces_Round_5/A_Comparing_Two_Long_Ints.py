# Link: https://codeforces.com/contest/616/problem/A
num1 = input()
num2 = input()

def determine_smaller(num1, num2):
    for n1, n2 in zip(num1, num2):
        if int(n1) < int(n2):
            print('<')
            return
        elif int(n2) < int(n1):
            print('>')
            return
    print('=')

if num1.startswith('0'):
    num1 = num1.lstrip('0')
if num2.startswith('0'):
    num2 = num2.lstrip('0')

if len(num1) > len(num2):
    print('>')
elif len(num2) > len(num1):
    print('<')
else:
    determine_smaller(num1, num2)
