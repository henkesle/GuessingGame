import unittest
from src.guessing_game import is_valid_target, generate_target, is_valid_guess, compare_guess


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

    def test_compare_guess_too_low(self):
        """Test that compare_guess returns 'too_low' when guess is less than target."""
        self.assertEqual(compare_guess(3, 5), "too_low")
        self.assertEqual(compare_guess(1, 999), "too_low")
        self.assertEqual(compare_guess(101, 501), "too_low")

    def test_compare_guess_too_high(self):
        """Test that compare_guess returns 'too_high' when guess is greater than target."""
        self.assertEqual(compare_guess(7, 5), "too_high")
        self.assertEqual(compare_guess(999, 1), "too_high")
        self.assertEqual(compare_guess(501, 101), "too_high")

    def test_compare_guess_correct(self):
        """Test that compare_guess returns 'correct' when guess equals target."""
        self.assertEqual(compare_guess(5, 5), "correct")
        self.assertEqual(compare_guess(1, 1), "correct")
        self.assertEqual(compare_guess(999, 999), "correct")
        self.assertEqual(compare_guess(501, 501), "correct")


if __name__ == '__main__':
    unittest.main()
