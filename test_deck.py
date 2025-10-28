"""Ghazal Tanavade
Unit tests for the Deck class.
"""

import unittest

from deck import Deck
from flashcard import Flashcard
from multiple_choice_card import MultipleChoiceCard
from true_false_card import TrueFalseCard


class TestDeck(unittest.TestCase):
    """Test cases for the Deck class."""

    def setUp(self):
        """Set up a deck and some cards for testing."""
        self.deck = Deck()
        self.card1 = Flashcard("What's Python?", "A programming language")
        self.card2 = MultipleChoiceCard(
            "Choose apple",
            "a",
            {"a": "Apple", "b": "Banana"}
        )
        self.card3 = TrueFalseCard("Ghazal's the GOAT", "t")

    def test_init(self):
        """Deck should be initialized empty."""
        self.assertEqual(self.deck.cards, [])

    def test_add_cards(self):
        """Test adding multiple cards to the deck."""
        self.deck.add_cards([self.card1, self.card2]) #adding two cards
        self.assertEqual(len(self.deck.cards), 2) #checking if length of deck is 2
        self.assertIn(self.card1, self.deck.cards)
        self.assertIn(self.card2, self.deck.cards)

        # Adding another card
        self.deck.add_cards([self.card3])
        self.assertEqual(len(self.deck.cards), 3) #checks if deck CONTAINS 3 cards
        self.assertIn(self.card3, self.deck.cards) #checking if card3 is in deck

    def test_str_empty(self):
        """Test string representation for empty deck."""
        self.assertEqual(str(self.deck), "")

    def test_str_nonempty(self):
        """Test string representation for non-empty deck."""
        self.deck.add_cards([self.card1, self.card2, self.card3])
        expected = (
         "1. What's Python?\n"
           "2. Choose apple\n"
          "3. Ghazal's the GOAT"
    )
        self.assertEqual(str(self.deck), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
