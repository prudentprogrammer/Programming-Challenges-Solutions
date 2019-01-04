def printStatus(actual_word, guessed_letters):
    correct_set = set(actual_word)
    so_far = set()
    wrong_set = set()

    for letter in guessed_letters:
        if letter in correct_set:
            so_far.add(letter)
            if so_far == correct_set:
                print('You win.')
                return
        else:
            wrong_set.add(letter)
            if len(wrong_set) >= 7:
                print('You lose.')
                return
    print('You chickened out.')

while True:
    roundNumber = int(input())
    if roundNumber == -1: # End of game
        break

    print('Round {}'.format(roundNumber))
    correct_word = input()
    guesses = input()
    printStatus(correct_word, guesses)
