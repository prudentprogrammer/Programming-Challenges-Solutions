from string import ascii_lowercase

for _ in range(int(input())):
    curr_line = input()
    counts = [0] * 26
    for char in curr_line:
        if char.isalpha():
            char = char.lower()
            counts[ord(char) - 97] += 1

    result = ascii_lowercase
    max_count = max(counts)
    print(''.join([result[ind] for ind, count in enumerate(counts) if count == max_count]))
