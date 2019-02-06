# Link: https://uva.onlinejudge.org/external/8/895.pdf

from collections import Counter

def get_total_words(words, curr_permutation):
    curr_permutation = Counter(''.join(curr_permutation))
    counter = 0
    for word_counter in words:
        nonlocal counter
        word_counter = word
        for k, v in word_counter.items():
            if k not in curr_permutation or curr_permutation[k] < v:
                return
        counter += 1

    [is_perm(word) for word in words]
    return counter

words = []
is_end_of_words = False
while True:
    curr_line = input()
    if curr_line == '#':
        if is_end_of_words:
            break
        is_end_of_words = True

    if not is_end_of_words:
        words.append(Counter(curr_line))
    else:
        if curr_line == '#':
            continue
        print(get_total_words(words, curr_line))
