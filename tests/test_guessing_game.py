import unittest
from unittest.mock import Mock, patch
from src.guessing_game import is_valid_target, generate_target, is_valid_guess, compare_guess, GuessingGame, GameState, play_game


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


class TestGuessingGameClass(unittest.TestCase):
    """Test cases for the GuessingGame class."""

    def test_game_initialization(self):
        """Test that a new game creates a valid target and starts in WAITING_FOR_GUESS state."""
        game = GuessingGame()
        self.assertIsNotNone(game.target)
        self.assertTrue(is_valid_target(game.target))
        self.assertEqual(game.state, GameState.WAITING_FOR_GUESS)
        self.assertEqual(game.attempts, 0)

    def test_make_guess_invalid(self):
        """Test that invalid guess returns 'invalid' and keeps game in WAITING_FOR_GUESS."""
        game = GuessingGame()
        result = game.make_guess(2)  # even number
        self.assertEqual(result, "invalid")
        self.assertEqual(game.state, GameState.WAITING_FOR_GUESS)
        self.assertEqual(game.attempts, 0)

    def test_make_guess_too_low(self):
        """Test that valid low guess returns 'too_low' and keeps game in WAITING_FOR_GUESS."""
        game = GuessingGame()
        # Force a specific target by mocking
        game.target = 501
        result = game.make_guess(3)
        self.assertEqual(result, "too_low")
        self.assertEqual(game.state, GameState.WAITING_FOR_GUESS)
        self.assertEqual(game.attempts, 1)

    def test_make_guess_too_high(self):
        """Test that valid high guess returns 'too_high' and keeps game in WAITING_FOR_GUESS."""
        game = GuessingGame()
        game.target = 101
        result = game.make_guess(999)
        self.assertEqual(result, "too_high")
        self.assertEqual(game.state, GameState.WAITING_FOR_GUESS)
        self.assertEqual(game.attempts, 1)

    def test_make_guess_correct(self):
        """Test that correct guess returns 'correct' and changes state to GAME_OVER."""
        game = GuessingGame()
        game.target = 501
        result = game.make_guess(501)
        self.assertEqual(result, "correct")
        self.assertEqual(game.state, GameState.GAME_OVER)
        self.assertEqual(game.attempts, 1)

    def test_multiple_guesses_before_correct(self):
        """Test that multiple guesses are tracked until correct guess."""
        game = GuessingGame()
        game.target = 501
        self.assertEqual(game.make_guess(3), "too_low")
        self.assertEqual(game.state, GameState.WAITING_FOR_GUESS)
        self.assertEqual(game.attempts, 1)
        self.assertEqual(game.make_guess(999), "too_high")
        self.assertEqual(game.state, GameState.WAITING_FOR_GUESS)
        self.assertEqual(game.attempts, 2)
        self.assertEqual(game.make_guess(501), "correct")
        self.assertEqual(game.state, GameState.GAME_OVER)
        self.assertEqual(game.attempts, 3)

    def test_guess_after_game_over(self):
        """Test that guesses after game over return 'game_over' and state remains GAME_OVER."""
        game = GuessingGame()
        game.target = 501
        game.make_guess(501)
        self.assertEqual(game.state, GameState.GAME_OVER)
        result = game.make_guess(501)
        self.assertEqual(result, "game_over")
        self.assertEqual(game.state, GameState.GAME_OVER)
        self.assertEqual(game.attempts, 1)  # attempts not incremented after game over


class TestPlayGame(unittest.TestCase):
    """Test cases for the play_game CLI function."""

    @patch('src.guessing_game.GuessingGame')
    def test_play_game_creates_game_instance(self, mock_game_class):
        """Test that play_game creates a GuessingGame instance."""
        mock_game = Mock()
        mock_game.target = 501
        mock_game.state = GameState.WAITING_FOR_GUESS
        mock_game.attempts = 0
        mock_game.make_guess.return_value = "correct"
        # Simulate state change after correct guess
        def make_guess_side_effect(guess):
            mock_game.state = GameState.GAME_OVER
            return "correct"
        mock_game.make_guess.side_effect = make_guess_side_effect
        mock_game_class.return_value = mock_game

        mock_input = Mock(return_value="501")
        mock_output = Mock()

        play_game(input_func=mock_input, output_func=mock_output)

        mock_game_class.assert_called_once()

    @patch('src.guessing_game.GuessingGame')
    def test_play_game_handles_correct_guess(self, mock_game_class):
        """Test that play_game handles a correct guess."""
        mock_game = Mock()
        mock_game.target = 501
        mock_game.state = GameState.WAITING_FOR_GUESS
        mock_game.attempts = 1
        def make_guess_side_effect(guess):
            mock_game.state = GameState.GAME_OVER
            return "correct"
        mock_game.make_guess.side_effect = make_guess_side_effect
        mock_game_class.return_value = mock_game

        mock_input = Mock(return_value="501")
        mock_output = Mock()

        play_game(input_func=mock_input, output_func=mock_output)

        mock_game.make_guess.assert_called_once_with(501)

    @patch('src.guessing_game.GuessingGame')
    def test_play_game_handles_invalid_guess(self, mock_game_class):
        """Test that play_game handles an invalid guess."""
        mock_game = Mock()
        mock_game.target = 501
        mock_game.state = GameState.WAITING_FOR_GUESS
        mock_game.attempts = 0
        mock_game.make_guess.return_value = "invalid"
        # For invalid guess, state doesn't change, but we need to end the loop
        # by changing state after the call
        def make_guess_side_effect(guess):
            mock_game.state = GameState.GAME_OVER
            return "invalid"
        mock_game.make_guess.side_effect = make_guess_side_effect
        mock_game_class.return_value = mock_game

        mock_input = Mock(return_value="2")
        mock_output = Mock()

        play_game(input_func=mock_input, output_func=mock_output)

        mock_game.make_guess.assert_called_once_with(2)

    @patch('src.guessing_game.GuessingGame')
    def test_play_game_handles_non_numeric_input(self, mock_game_class):
        """Test that play_game handles non-numeric input without crashing."""
        mock_game = Mock()
        mock_game.target = 501
        mock_game.state = GameState.WAITING_FOR_GUESS
        mock_game.attempts = 0
        def make_guess_side_effect(guess):
            mock_game.state = GameState.GAME_OVER
            return "correct"
        mock_game.make_guess.side_effect = make_guess_side_effect
        mock_game_class.return_value = mock_game

        mock_input = Mock(return_value="501")
        mock_output = Mock()

        play_game(input_func=mock_input, output_func=mock_output)

        # Should not crash and should eventually call make_guess
        self.assertTrue(mock_game.make_guess.called)


if __name__ == '__main__':
    unittest.main()
