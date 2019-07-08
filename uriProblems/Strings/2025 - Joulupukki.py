import string
for _ in range(int(input())):
    curr_line = input()
    words = curr_line.split()
    replaced_words = {}
    for word in words:
        word = word.translate(word.maketrans('', '', string.punctuation))
        if len(word) >= 10 and word[1:-1] == 'oulupukk':
            replaced_words[word] = 'Joulupukki'

    for k, v in replaced_words.items():
        curr_line = curr_line.replace(k, v)
    print(curr_line)
