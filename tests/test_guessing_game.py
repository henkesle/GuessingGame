import unittest
from src.guessing_game import is_valid_target


class TestGuessingGame(unittest.TestCase):
    """Test cases for the odd integer guessing game."""

    def test_valid_odd_numbers_in_range(self):
        """Test that valid odd numbers between 1 and 1000 are accepted."""
        self.assertTrue(is_valid_target(1))
        self.assertTrue(is_valid_target(3))
        self.assertTrue(is_valid_target(999))

    def test_invalid_even_numbers(self):
        """Test that even numbers are rejected."""
        self.assertFalse(is_valid_target(2))
        self.assertFalse(is_valid_target(4))
        self.assertFalse(is_valid_target(1000))

    def test_invalid_numbers_below_range(self):
        """Test that numbers below 1 are rejected."""
        self.assertFalse(is_valid_target(0))
        self.assertFalse(is_valid_target(-1))
        self.assertFalse(is_valid_target(-100))

    def test_invalid_numbers_above_range(self):
        """Test that numbers above 1000 are rejected."""
        self.assertFalse(is_valid_target(1001))
        self.assertFalse(is_valid_target(1002))
        self.assertFalse(is_valid_target(2000))

    def test_invalid_non_integer_types(self):
        """Test that non-integer types are rejected."""
        self.assertFalse(is_valid_target(3.5))
        self.assertFalse(is_valid_target("5"))
        self.assertFalse(is_valid_target(None))


if __name__ == '__main__':
    unittest.main()
