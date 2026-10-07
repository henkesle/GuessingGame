import random
from enum import Enum


def is_valid_target(value):
    """Check if a value is a valid game target (odd integer between 1 and 1000)."""
    # Check if value is an integer
    if not isinstance(value, int):
        return False
    
    # Check if value is in range [1, 1000]
    if value < 1 or value > 1000:
        return False
    
    # Check if value is odd
    if value % 2 == 0:
        return False
    
    return True


def generate_target():
    """Generate a random valid target (odd integer between 1 and 999)."""
    # Generate a random number from 0 to 499 (500 possible odd numbers)
    # Multiply by 2 and add 1 to get odd numbers from 1 to 999
    return random.randint(0, 499) * 2 + 1


def is_valid_guess(value):
    """Check if a player's guess is valid (odd integer between 1 and 1000)."""
    return is_valid_target(value)


def compare_guess(guess, target):
    """Compare a guess to the target and return the result."""
    if guess < target:
        return "too_low"
    elif guess > target:
        return "too_high"
    else:
        return "correct"


class GameState(Enum):
    """Enumeration representing the possible states of the guessing game."""
    WAITING_FOR_GUESS = 1
    GAME_OVER = 2


class GuessingGame:
    """A class that manages a guessing game with a target number."""

    def __init__(self):
        """Initialize a new game with a random target."""
        self.target = generate_target()
        self.state = GameState.WAITING_FOR_GUESS
        self.attempts = 0

    def make_guess(self, guess):
        """Process a player's guess and return the result."""
        if self.state == GameState.GAME_OVER:
            return "game_over"

        if not is_valid_guess(guess):
            return "invalid"

        self.attempts += 1
        result = compare_guess(guess, self.target)

        if result == "correct":
            self.state = GameState.GAME_OVER

        return result


def play_game(input_func=input, output_func=print):
    """Play a guessing game with the given input and output functions."""
    game = GuessingGame()
    output_func("Welcome to the Odd Integer Guessing Game!")
    output_func("I'm thinking of an odd integer between 1 and 1000.")
    output_func("Try to guess it!")

    while game.state == GameState.WAITING_FOR_GUESS:
        output_func("Enter your guess: ", end="")
        try:
            user_input = input_func()
        except EOFError:
            output_func("\nGame ended.")
            break
        
        # Try to convert input to integer
        try:
            guess = int(user_input)
        except ValueError:
            output_func("Invalid input. Please enter an integer.")
            continue

        result = game.make_guess(guess)

        if result == "invalid":
            output_func("Invalid guess. Please enter an odd integer between 1 and 1000.")
        elif result == "too_low":
            output_func("Too low! Try again.")
        elif result == "too_high":
            output_func("Too high! Try again.")
        elif result == "correct":
            output_func(f"Correct! You guessed the number in {game.attempts} attempts!")
        elif result == "game_over":
            output_func("The game is already over.")


if __name__ == "__main__":
    play_game()
