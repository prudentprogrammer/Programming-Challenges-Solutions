# Link: https://uva.onlinejudge.org/external/112/11278.pdf
from sys import stdin

qwerty = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "
dvorak = "`123qjlmfp/[]456.orsuyb;=\\789aehtdck-0zx,inwvg'~!@#QJLMFP?{}$%^>ORSUYB:+|&*(AEHTDCK_)ZX<INWVG\" "

# Construct the mapping
keyboardMap = {qwertyLetter: dvorakLetter for qwertyLetter,dvorakLetter in zip(qwerty, dvorak) }

for line in stdin:
  print(''.join([keyboardMap[x] for x in line.strip('\n')]))

# FOR REFERENCE:
# qwerty = [
#   '`1234567890-=',
#   'qwertyuiop[]\\',
#   'asdfghjkl;\'',
#   'zxcvbnm,./',
#   '~!@#$%^&*()_+',
#   'QWERTYUIOP{}|',
#   'ASDFGHJKL:"',
#   'ZXCVBNM<>? '
# ]
#
# dvorak = [
#   '`123qjlmfp/[]',
#   '456.orsuyb;=\\',
#   '789aehtdck-',
#   "0zx,inwvg'",
#   '~!@#QJLMFP?{}',
#   '$%^>ORSUYB:+|',
#   '&*(AEHTDCK_',
#   ')ZX<INWVG" '
# ]