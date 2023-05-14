# The word to be guessed
WORD = 'SNAKE'

# Allow the user to guess up to 6 times
for guess_num in range(1, 7):

    # Prompt the user for a guess
    guess = input(f'\nGuess {guess_num}: ').upper()

    # If the guess is correct, end the game
    if guess == WORD:
        print('Correct')
        break

    # Save in sets the correct, misplaced and wrong letters in the guess
    correct_letters     = set(letter for letter, correct in zip(guess, WORD) if letter == correct)
    misplaced_letters   = set(guess) & set(WORD) - correct_letters
    wrong_letters       = set(guess) - set(WORD)

    # Display tips for help the user
    print('Correct letters:',   ', '.join(sorted(correct_letters)))
    print('Misplaced letters:', ', '.join(sorted(misplaced_letters)))
    print('Wrong letters:',     ', '.join(sorted(wrong_letters)))
