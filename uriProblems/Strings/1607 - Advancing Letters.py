for _ in range(int(input())):
    word1, word2 = input().split()
    temp = 0
    for a,b in zip(word1, word2):
        diff = ord(b) - ord(a)
        if diff < 0:
            diff = diff + 26
        temp += diff
    print(temp)
