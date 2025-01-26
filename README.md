# Hangman-Game

## Overview

Welcome to the Hangman Game! This is a classic word-guessing game where players attempt to reveal the hidden word by guessing one letter at a time. Be careful, though – too many wrong guesses and the hangman is complete!

## Features

A pre-defined word list to choose the hidden word from.

ASCII art representing the hangman’s progression.

Validation for user input to ensure smooth gameplay.

Tracks incorrect guesses and remaining chances.

Congratulates the player upon success or reveals the correct word if the game is lost.

## How It Works

A random word is selected from the list of possible words.

The word is hidden, and the player must guess letters to reveal it.

Each incorrect guess reduces the number of remaining chances.

The game ends when:

The player guesses the word correctly.

The hangman is completed after 6 incorrect guesses.

## Game Rules

Only uppercase English letters (A-Z) are allowed.

You can guess one letter at a time.

Letters already guessed will not reduce the remaining chances.

## How to Play

1. Clone this repository:

git clone https://github.com/yultis/Hangman-Game.git

2. Navigate to the project directory:

cd Hangman-Game

3. Run the game script:

python hangman_game.py

4. Follow the on-screen instructions to play the game.

## Code Details

The game is implemented in Python and includes:

Word List: A collection of words relevant to technology and data.

Hangman Images: ASCII art representing the hangman figure at different stages.

Game Logic: Tracks player progress, validates input, and manages game states.

## Example Output

### Start of Game

Welcome to HANGMAN GAME!

Hidden word is: _ _ _ _ _ _

Failed letters:

Pick a letter:

### Correct Guess

CORRECT! The word contains the letter A!

Hidden word is: A _ A _ Y _

### Incorrect Guess

WRONG! Number of mistakes left: 5

End of Game

#### Win:

CONGRATULATIONS! You guessed the word!

#### Lose:

HANGED!! Better luck next time!
The correct word is: PYTHON

## Conclusion

This Hangman game is a fun and interactive way to test your word-guessing skills. The project is an excellent starting point for Python beginners to learn about loops, conditionals, and string manipulation. Happy playing!

## License

This project is licensed under the MIT License. See the LICENSE file for details.