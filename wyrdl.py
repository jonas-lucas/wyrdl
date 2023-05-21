# Import essentials libraries
import pathlib
import random

from string import ascii_letters
from typing import List

from rich.console import Console
from rich.theme import Theme

console = Console(width=40, theme=Theme({'warning': 'red on yellow'}))

def main():
    """Main function to run the word guessing game."""

    # Pre-process: Load the word list and choose a random word
    words_path = pathlib.Path(__file__).parent / 'wordlist.txt'
    word = get_random_word(words_path.read_text(encoding='utf-8').split('\n'))
    guesses = ['_' * 5] * 6

    # Process (main loop): Allow the user to make guesses and provide feedback
    for idx in range(6):
        refresh_page(headline=f'Guess {idx + 1}')
        show_guesses(guesses, word)

        guesses[idx] = input(f'\nGuess word: ').upper() # Prompt the user for a guess
        
        if guesses[idx] == word: # If the guess is correct, end the game
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

def show_guesses(guesses: List[str], word: str) -> None:
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = 'bold white on green'
            elif letter in word:
                style = 'bold white on yellow'
            elif letter in ascii_letters:
                style = 'white on #666666'
            else:
                style = 'dim'
            styled_guess.append(f'[{style}]{letter}[/]')

        console.print(''.join(styled_guess), justify='center')

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

def refresh_page(headline):
    console.clear()
    console.rule(f'[bold blue]:leafy_green: {headline} :leafy_green:[/]\n')

if __name__ == '__main__':
    main()
