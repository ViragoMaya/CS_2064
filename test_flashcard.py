"""Ghazal Tanavade
Unit tests for the Flashcard class.
"""

import unittest

from flashcard import Flashcard


class TestFlashcard(unittest.TestCase):
    """Test cases for the Flashcard class."""

    def setUp(self):
        """Settung up test functions before each test method."""
        self.flashcard = Flashcard("What is the value of 8 % 3 * 2", "4")

    def test_init(self):
        """Test flashcard initialization."""
        self.assertEqual(self.flashcard.prompt, "What is the value of 8 % 3 * 2")
        self.assertEqual(self.flashcard.response, "4")

    def test_str(self):
        """Test string representation of flashcard."""
        expected = "Answer: 4"
        self.assertEqual(str(self.flashcard), expected)

    def test_check_answer_correct(self):
        """Test check_answer with correct answer."""
        self.assertTrue(self.flashcard.check_answer("4"))

    def test_check_answer_correct_ci(self):
        """Test check_answer is case insensitive."""
        card = Flashcard("Are Dictionary keys mutable or immutable?", "Immutable")
        self.assertTrue(card.check_answer("immutable"))
        self.assertTrue(card.check_answer("IMMUTABLE"))

    def test_check_answer_incorrect(self):
        """Test check_answer with incorrect answer."""
        self.assertFalse(self.flashcard.check_answer("5"))

    def test_get_options(self):
        """Test get_options returns correct list."""
        expected = ["Fill in the blank"]
        self.assertEqual(self.flashcard.get_options(), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
