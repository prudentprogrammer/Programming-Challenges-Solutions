
def printStatus(actual_word, guessed_letters):
    actual_word_diff = len(set(actual_word) - set(guessed_letters))
    guessed_letters_diff = len(set(guessed_letters) - set(actual_word))

    if actual_word_diff == 0 and guessed_letters_diff < 7:
        print('You win.')
    elif guessed_letters_diff >= 7:
        print('You lose.')
    else:
        print('You chickened out.')

while True:
    roundNumber = int(input())
    if roundNumber == -1: # End of game
        break

    print('Round {}'.format(roundNumber))
    correct_word = input()
    guesses = input()
    printStatus(correct_word, guesses)
