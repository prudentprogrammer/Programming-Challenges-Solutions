# Link: https://uva.onlinejudge.org/external/15/1584.pdf
import re

def get_smallest_lex_dna(dna):
    for nucleotide in 'ACGT':
        all_indices = [m.start() for m in re.finditer(nucleotide, dna)]
        if all_indices:
            return sorted([dna[index:] + dna[:index] for index in all_indices])[0]

for _ in range(int(input())):
    print(get_smallest_lex_dna(input()))
