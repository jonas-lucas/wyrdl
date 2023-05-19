# Import essentials libraries
import pathlib
import random
from string import ascii_letters
from typing import List

def main():
    """Main function to run the word guessing game."""

    # Pre-process: Load the word list and choose a random word
    words_path = pathlib.Path(__file__).parent / 'wordlist.txt'
    word = get_random_word(words_path.read_text(encoding='utf-8').split('\n'))

    # Process (main loop): Allow the user to make guesses and provide feedback
    for guess_num in range(1, 7):
        guess = input(f'\nGuess {guess_num}: ').upper() # Prompt the user for a guess
        
        show_guess(guess, word)
        if guess == word: # If the guess is correct, end the game
            break
    
    # Post-process: Finish the game
    else:
        game_over(word)

def get_random_word(word_list: List[str]) -> str:
    """Get a random five-letter word from a list of strings.
    
    Args:
        word_list (List[str]): List of words.

    Returns:
        str: Random five-letter word from the list.

    Example:
        >>> get_random_word(["snake", "worm", "it\'ll"])
        'SNAKE'
    """

    # Load valid words from the wordlist file
    words = [
        word.upper() for word in word_list
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]

    # Return a random word from the loaded word list
    return random.choice(words)

def show_guess(guess: str, word: str) -> None:
    """Show the user's guess on the terminal and classify all letters.
    
    Args:
        guess (str): User's guess.
        word (str): The correct word.

    Returns:
        None

    Example:
        >>> show_guess('CRANE', 'SNAKE')
        Correct letters: A, E
        Misplaced letters: N
        Wrong letters: C, R
    """

    # Classify the letters in the guess as correct, misplaced and wrong
    correct_letters     = set(letter for letter, correct in zip(guess, word) if letter == correct)
    misplaced_letters   = set(guess) & set(word) - correct_letters
    wrong_letters       = set(guess) - set(word)

    # Display the classification of letters
    print('Correct letters:',   ', '.join(sorted(correct_letters)))
    print('Misplaced letters:', ', '.join(sorted(misplaced_letters)))
    print('Wrong letters:',     ', '.join(sorted(wrong_letters)))

def game_over(word: str) -> None:
    """Show the correct word after the game ends.
    
    Args:
        word (str): The correct word.

    Returns:
        None
    
    Example:
        >>> game_over('SNAKE')
        The word was SNAKE
    """

    # Reveal the correct word
    print(f'The word was {word}')

if __name__ == '__main__':
    main()
