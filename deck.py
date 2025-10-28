"""Ghazal Tanavade

Deck class for the Flashcard system.
"""

class Deck:
    """Holds a collection of flashcard objects.

    Attributes:
        cards (list): A list to hold all the cards.

    """

    def __init__(self):
        """Initialize empty deck/list."""
        self.cards = []

    def __str__(self):
        """Return a formatted string listing all cards in the deck.
        Each line includes the card number and its prompt.
        """
        result = ""
        # Loops through each card in deck giving both the card and its index
        for idx, card in enumerate(self.cards, 1):
            #eg. number.(space)<question prompt>
            result += f"{idx}. {card.prompt}\n"
        return result.strip()

    def add_cards(self, cards):
        """Append each card from the input list to the deck's cards list.

        Args:
            cards (list): A list of card objects to add.

        """
        for card in cards:
            self.cards.append(card)
