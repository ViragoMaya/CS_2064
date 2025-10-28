"""Ghazal Tanavade
Unit tests for the StudySession class.
"""

import unittest
from io import StringIO
from unittest.mock import patch

from deck import Deck
from multiple_choice_card import MultipleChoiceCard
from study_session import StudySession
from true_false_card import TrueFalseCard


class TestStudySession(unittest.TestCase):
    """Test cases for the StudySession class."""

    def setUp(self):
        """Set up a deck and study session with three cards."""
        self.deck = Deck()
        self.deck.add_cards([
        MultipleChoiceCard(
            "Which animal is the Python programming language named after?",
            "c",
            {
                "a": "Tiger",
                "b": "Snake",
                "c": "Monty Python"
            }
        ),
        TrueFalseCard("True of False: Ghazal is da #goat", "t"),
        MultipleChoiceCard(
            "Which of these is a valid Python variable name?",
            "b",
            {
                "a": "2cool4school",
                "b": "cool_var",
                "c": "hello-world!"
            }
        ),
    ])
        self.ss = StudySession(self.deck)

    def test_init(self):
        """Test initialization of StudySession.
        Checks that the session starts with the correct deck and zero counts.
        """
        self.assertEqual(self.ss.deck, self.deck)
        self.assertEqual(self.ss.correct, 0)
        self.assertEqual(self.ss.total, 0)

    def test_str_zero(self):
        """Test __str__ before any questions answered."""
        self.assertEqual(str(self.ss), "Study Session not started")

    def test_str_nonzero(self):
        """Test __str__ after answering some questions."""
        self.ss.correct = 2
        self.ss.total = 3
        self.assertEqual(str(self.ss), "67%") #rounded percentage

    #patching input to simulate user answers
    #Mock user input: q1 wrong, q2 wrong->right, q3 right.
    @patch(
    'builtins.input',
    side_effect=['a', 'b', 'f', 't', 'b']
)
    def test_start(self, mock_input):
        """Test the start method with simulated user input.
        Simulates a user getting two cards right and one wrong.
        """
        #replaces terminal output with StringIO object buffer
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ss.start()
            result = fake_out.getvalue()
        # Check the summary is printed and percent is correct
        self.assertIn("67%", result)
        self.assertIn("Correct   : 2", result)
        self.assertIn("Questions : 3", result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
