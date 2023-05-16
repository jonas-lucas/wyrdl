# Import essentials libraries
import pathlib
import random
from string import ascii_letters

# File path of the file 'wordlist.txt'
WORDLIST = pathlib.Path('wordlist.txt')

# Load valid words from the wordlist file
words = [
    word.upper()
    for word in WORDLIST.read_text(encoding='utf-8').strip().split('\n')
    if len(word) == 5 and all(letter in ascii_letters for letter in word)
]

# Select a random word from the loaded word list
word = random.choice(words)

# Allow the user to guess up to 6 times
for guess_num in range(1, 7):

    # Prompt the user for a guess
    guess = input(f'\nGuess {guess_num}: ').upper()

    # If the guess is correct, end the game
    if guess == word:
        print('Correct')
        break

    # Save in sets the correct, misplaced and wrong letters in the guess
    correct_letters     = set(letter for letter, correct in zip(guess, word) if letter == correct)
    misplaced_letters   = set(guess) & set(word) - correct_letters
    wrong_letters       = set(guess) - set(word)

    # Display tips for help the user
    print('Correct letters:',   ', '.join(sorted(correct_letters)))
    print('Misplaced letters:', ', '.join(sorted(misplaced_letters)))
    print('Wrong letters:',     ', '.join(sorted(wrong_letters)))
else:
    # If the user fails to guess within the allowed attempts, reveal the correct word
    print(f'The word was {word}')
