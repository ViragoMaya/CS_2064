"""Ghazal Tanavade
Unit tests for the MultipleChoiceCard class.
"""

import unittest

from multiple_choice_card import MultipleChoiceCard


class TestMultipleChoiceCard(unittest.TestCase):
    """Test cases for the MultipleChoiceCard class."""

    def setUp(self):
        """Set up a MultipleChoiceCard for testing."""
        self.choices = {
            'a': 'Error handling',
            'b': 'Looping',
            'c': 'Variable assignment'
        }
        self.card = MultipleChoiceCard(
            "Which of the following best describes the purpose of a "
            "try-except block in Python?",
            "a",
            self.choices
        )

    def test_init(self):
        """Test initialization of MultipleChoiceCard."""
        self.assertEqual(
            self.card.prompt,
            "Which of the following best describes the purpose of a "
            "try-except block in Python?"
        )
        self.assertEqual(self.card.response, "a")
        self.assertEqual(self.card.choices, self.choices)

    def test_str(self):
        """Test string representation (__str__)"""
        expected = "Answer: a"
        self.assertEqual(str(self.card), expected)

    def test_check_answer_correct(self):
        """Test check_answer returns True for correct answer."""
        self.assertTrue(self.card.check_answer("a"))

    def test_check_answer_incorrect(self):
        """Test check_answer returns False for incorrect answer."""
        self.assertFalse(self.card.check_answer("b"))
        self.assertFalse(self.card.check_answer("Looping"))  # Only label is correct

    def test_check_answer_case_insensitive(self):
        """Test check_answer is case insensitive."""
        card = MultipleChoiceCard("Question_Placeholder", "b", {'a': 'No', 'b': 'Yes'})
        self.assertTrue(card.check_answer("B"))
        self.assertTrue(card.check_answer("b"))
        self.assertFalse(card.check_answer("c"))

    def test_display(self):
        """Test display outputs correct lines (uses print)."""
        # Capture output from print using StringIO
        # redirecting sys.stdoubt to StrinIO buffer so print output coudl be checked.
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            self.card.display()
            output = out.getvalue()
        finally:
            sys.stdout = saved_stdout

        self.assertEqual(
        self.card.prompt,
        "Which of the following best describes the purpose of a "
        "try-except block in Python?"
    )
        self.assertIn("a: Error handling", output)
        self.assertIn("b: Looping", output)
        self.assertIn("c: Variable assignment", output)

    def test_get_options(self):
        """Test get_options returns labels as a list."""
        expected = ['a', 'b', 'c']
        self.assertEqual(self.card.get_options(), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
