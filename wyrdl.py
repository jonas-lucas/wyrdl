# Import essentials libraries
import pathlib
import random

from string import ascii_letters
from typing import List

from rich.console import Console
from rich.theme import Theme

console = Console(width=40, theme=Theme({'warning': 'red on yellow'})) # Instance the console

def main():
    """Main function to run the word guessing game."""

    # Pre-process: Load the word list and choose a random word
    words_path = pathlib.Path(__file__).parent / 'wordlist.txt'
    word = get_random_word(words_path.read_text(encoding='utf-8').split('\n'))
    guesses = ['_' * 5] * 6

    # Process (main loop): Allow the user to make guesses and provide feedback
    for idx in range(6):
        refresh_page(headline=f'Guess {idx + 1}') # Refresh the page with a new headline
        show_guesses(guesses, word) # Display the current state of guesses

        guesses[idx] = guess_word(previous_guesses=guesses[:idx]) # Prompt the user for a guess
        
        if guesses[idx] == word: # If the guess is correct, end the game
            break
    
    # Post-process: Finish the game
    game_over(guesses, word, guessed_correctly=guesses[idx] == word)

def refresh_page(headline: str) -> None:
    """Clears the console and prints the provided headline as the new header."""
    console.clear() # Clear the console
    console.rule(f'[bold blue]:leafy_green: {headline} :leafy_green:[/]\n') # Print header

def get_random_word(word_list: List[str]) -> str:
    """Returns a random word from the given list of the words, filtered by length and character
    requirements."""
    # Load valid words from the wordlist file 
    if words := [
        word.upper() for word in word_list
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]:
        # Return a random word from the loaded word list
        return random.choice(words) 
    else:
        # Return an error and end the game
        console.print('No words of length 5 in the word list', style='warning')
        raise SystemExit()

def show_guesses(guesses: List[str], word: str) -> None:
    """Prints the current state of guesses, highlighting correct, misplaced, and wrong letters."""
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, word): # Check letter by letter
            if letter == correct:
                style = 'bold white on green' # If correct
            elif letter in word:
                style = 'bold white on yellow' # If misplaced
            elif letter in ascii_letters:
                style = 'white on #666666' # If wrong
            else:
                style = 'dim' # Normal style
            styled_guess.append(f'[{style}]{letter}[/]') # Save styled previous guesses

        # Print styled previous guesses
        console.print(''.join(styled_guess), justify='center') 

def guess_word(previous_guesses):
    """Prompts the user to enter a guess and performs input validation."""
    guess = console.input('\nGuess word: ').upper() # Prompt the user for a guess

    # Check if the guess is repeatable
    if guess in previous_guesses:
        console.print(f'You\'ve already guessed {guess}.', style='warning')
        return guess_word(previous_guesses)

    # Check if the guess length is not 5 
    if len(guess) != 5:
        console.print('Your guess must be 5 letters.', style='warning')
        return guess_word(previous_guesses)

    # Check if the guess is a letter
    if any((invalid := letter) not in ascii_letters for letter in guess):
        console.print(
            f'Invalid letter: \'{invalid}\'. Please use English letters.',
            style='warning',
        )
        return guess_word(previous_guesses)

    return guess # Return correct input

def game_over(guesses: List[str], word: str, guessed_correctly: bool) -> None:
    """Prints the game over screen, displaying the guesses and whether the word was guessed 
    correctly."""
    refresh_page(headline='Game Over')
    show_guesses(guesses, word)

    if guessed_correctly: # If the word was guessed correctly
        console.print(f'\n[bold white on green]Correct, the word is {word}[/]')
    else: # If the word was not guessed correctly
        console.print(f'\n[bold white on red]Sorry, the word was {word}[/]')

if __name__ == '__main__':
    main()
