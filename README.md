# Odd Integer Guessing Game

A simple Python command-line game where the player tries to guess a randomly generated odd integer between 1 and 1000.

## Project Structure

```
GuessingGame/
├── src/
│   ├── __init__.py
│   └── guessing_game.py
├── tests/
│   ├── __init__.py
│   └── test_guessing_game.py
├── README.md
├── .gitignore
└── requirements.txt
```

## How to Run the Game

From the project root directory, run:

```
python src/guessing_game.py
```

The game will ask the player to enter an odd integer between 1 and 1000.

- If the guess is too low, the game will indicate that the guess was too low.
- If the guess is too high, the game will indicate that the guess was too high.
- If the guess is correct, the game ends and displays the number of attempts.
- Invalid or non-numeric input is handled without crashing the game.

## Running Tests

The project uses Python's built-in `unittest` framework.

To run the complete test suite:

```
python -m unittest discover tests
```

You can also run the test file directly:

```
python tests/test_guessing_game.py
```

The test suite covers target validation, target generation, guess validation, guess comparison, game-state management, attempt tracking, and command-line game behavior.

## Development

This project was developed using Test-Driven Development (TDD). Tests were written and run during each development stage before implementing the corresponding functionality.

The project uses a combination of procedural functions and object-oriented programming. The `GuessingGame` class manages game state and gameplay, while separate functions handle validation, target generation, and guess comparison.
