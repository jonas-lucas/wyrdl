# Import essentials libraries
import pathlib
import sys
from string import ascii_letters

# If the command-line arguments are valid
if len(sys.argv) >= 3:
    # Get the input and output file paths from the command-line arguments
    in_path = pathlib.Path(sys.argv[1])
    out_path = pathlib.Path(sys.argv[2])

    # Read words from the input file
    words = sorted(
        {
            word.lower()
            for word in in_path.read_text(encoding='utf-8').split()
            if all(letter in ascii_letters for letter in word) # Filter the words
        },
        key=lambda word: (len(word), word), # Sort the words
    )

    # Write the filtered and sorted words to the ouput file
    out_path.write_text('\n'.join(words))
else:
    # Display an error if input and output file paths are not provided
    print('Please provide input and output file paths as command-line arguments.')
