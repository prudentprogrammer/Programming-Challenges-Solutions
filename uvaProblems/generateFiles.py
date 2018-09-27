allFiles = """UVa 12015 - Google is Feeling Lucky
UVa 12157 - Tariff Plan
UVa 12468 - Zapping
UVa 12503 - Robot Instructions
UVa 12554 - A Special Song
IOI 2010 - Cluedo
IOI 2010 - Memory
UVa 00119 - Greedy Gift Givers
UVa 00573 - The Snail Simulation
UVa 00661 - Blowing Fuses
UVa 10141 - Request for Proposal
UVa 10324 - Zeros and Ones
UVa 10424 - Love Calculator
UVa 10919 - Prerequisites
UVa 11507 - Bender BRodriguez
UVa 11586 - Train Tracks
UVa 11661 - Burger Time
UVa 11683 - Laser Sculpture
UVa 11687 - Digits
UVa 11956 - Brainfrick
UVa 12478 - Hardest Problem
IOI 2009 - Garage
IOI 2009 - POI""".split('\n')
print(allFiles)

for file in allFiles:
  problemNumber, _, problemName = file.partition('-')
  fileName = '{} {}.py'.format(problemNumber.strip().split()[-1], problemName.strip())
  f = open(fileName, "w+")
  stringToWrite = r"""# Link: 

for _ in range(int(input())):
  pass
  """
  f.write(stringToWrite)
  f.close()