"""Ghazal Tanavade
Unit tests for the TrueFalseCard class.
"""

import unittest

from true_false_card import TrueFalseCard


class TestTrueFalseCard(unittest.TestCase):
    """Test cases for the TrueFalseCard class."""

    def test_constructor(self):
        """Test that the TrueFalseCard constructor stores values correctly."""
        card = TrueFalseCard("Is Python dynamically typed?", "t")
        self.assertEqual(card.prompt, "Is Python dynamically typed?")
        self.assertEqual(card.response, "t")
        # Checking choices in dict are correct
        expected_choices = {"t": "true", "f": "false"}
        self.assertEqual(card.choices, expected_choices)

if __name__ == '__main__':
    unittest.main(verbosity=2)
