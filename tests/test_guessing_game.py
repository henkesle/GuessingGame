import unittest
from src.guessing_game import is_valid_target, generate_target, is_valid_guess


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

    def test_generate_target_returns_integer(self):
        """Test that generate_target returns an integer."""
        target = generate_target()
        self.assertIsInstance(target, int)

    def test_generate_target_is_valid(self):
        """Test that generate_target returns a valid target using is_valid_target."""
        target = generate_target()
        self.assertTrue(is_valid_target(target))

    def test_generate_target_multiple_calls(self):
        """Test that generate_target produces valid targets across multiple calls."""
        targets = [generate_target() for _ in range(10)]
        for target in targets:
            self.assertTrue(is_valid_target(target), f"Generated invalid target: {target}")

    def test_generate_target_range(self):
        """Test that generate_target produces values within the expected range."""
        target = generate_target()
        self.assertGreaterEqual(target, 1)
        self.assertLessEqual(target, 999)

    def test_valid_odd_guesses(self):
        """Test that valid odd guesses are accepted."""
        self.assertTrue(is_valid_guess(1))
        self.assertTrue(is_valid_guess(3))
        self.assertTrue(is_valid_guess(501))
        self.assertTrue(is_valid_guess(999))

    def test_invalid_even_guesses(self):
        """Test that even guesses are rejected."""
        self.assertFalse(is_valid_guess(2))
        self.assertFalse(is_valid_guess(4))
        self.assertFalse(is_valid_guess(1000))

    def test_invalid_guesses_below_range(self):
        """Test that guesses below 1 are rejected."""
        self.assertFalse(is_valid_guess(0))
        self.assertFalse(is_valid_guess(-1))
        self.assertFalse(is_valid_guess(-100))

    def test_invalid_guesses_above_range(self):
        """Test that guesses above 1000 are rejected."""
        self.assertFalse(is_valid_guess(1001))
        self.assertFalse(is_valid_guess(1002))
        self.assertFalse(is_valid_guess(2000))

    def test_invalid_non_integer_guesses(self):
        """Test that non-integer guesses are rejected."""
        self.assertFalse(is_valid_guess(3.5))
        self.assertFalse(is_valid_guess("5"))
        self.assertFalse(is_valid_guess(None))


if __name__ == '__main__':
    unittest.main()
