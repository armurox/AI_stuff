# Crossword Puzzle Generator

This Python program generates crossword puzzles based on a specified crossword structure and word list. It employs Constraint Satisfaction Problem (CSP) techniques to find valid word assignments for the puzzle variables.

## Files

- `crossword.py`: Defines classes and functions for representing crossword puzzles and their constraints.
- `generate.py`: Contains the main logic for generating crossword puzzles using CSP techniques.

## Techniques used
- Backtrack search
- ac3 for arc consistency
- node consistency was also enforced

## Usage

To generate a crossword puzzle, run the `generate.py` script from the command line with the following arguments:

```shell
python3 generate.py structure words [output]
```

- `structure`: The path to a text file that defines the crossword puzzle structure. Use underscores `_` to represent blank squares and other characters for blocked squares.

Example `structure` file:
```
__A____
___X___
_______
___Y___
__B____
```

- `words`: The path to a text file containing a list of words to be used for filling in the puzzle. Each word should be on a separate line in uppercase.

Example `words` file:
```
APPLE
BANANA
XYLOPHONE
```

- `output` (optional): The path to an image file where the generated crossword puzzle will be saved as an image. Supported image formats include PNG, JPEG, and others.

## How It Works

1. The program reads the crossword structure and word list from the provided files.

2. It initializes a CSP crossword generator, creating variables for each blank square in the structure and assigning the initial domain of candidate words for each variable.

3. The CSP solver enforces node consistency by removing words from the domain of each variable that do not match the required length.

4. It then enforces arc consistency by checking if there are any words in the domains of two variables that cannot be assigned together based on their overlapping positions.

5. The CSP solver proceeds with backtracking search, recursively attempting to assign words to variables while ensuring consistency with the crossword structure and previously assigned words.

6. If a valid assignment is found, the program prints the crossword puzzle to the terminal and, if an `output` file is specified, saves the puzzle as an image.

## Dependencies

- Python 3.x
- PIL (Python Imaging Library): Used for saving the crossword puzzle as an image.

Install PIL using the following command:

```shell
pip3 install pillow
```

## Example

To generate a crossword puzzle using the provided `structure` and `words` files, run the following command:

```shell
python generate.py structure.txt words.txt crossword.png
```

This will create a crossword puzzle and save it as `crossword.png`.

## License

This crossword puzzle generator is provided under the [MIT License](LICENSE).

---

Please note that all functions in crossword.py came with the assignment starter code and are not my work. Starter code ©2023 Brian Yu/ Harvard 2023.
