vowels = [letter for letter in input() if letter in ['a', 'e', 'i', 'o', 'u']]
print(['N', 'S'][vowels[::-1] == vowels])