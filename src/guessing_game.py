import random


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
