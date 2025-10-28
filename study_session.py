"""Ghazal Tanavade

StudySession class for the Flashcard quiz system.
"""

class StudySession:
    """Manages a study session using a deck of flashcards.

    Attributes:
        deck (Deck): The deck of cards to study.
        correct (int): Number of correctly answered questions.
        total (int): Total number of questions asked.

    """

    def __init__(self, deck):
        """Initialize a study session.

        Args:
            deck (Deck): The deck to use for the session.

        """
        self.deck = deck
        self.correct = 0
        self.total = 0

    def __str__(self):
        """Return the percent correct, rounded to nearest whole number, followed by %.
        If no questions have been asked, returns "Study Session not started".
        """
        if self.total == 0:
            return "Study Session not started"
        percent = round((self.correct / self.total) * 100) # correct percentage
        return f"{percent}%"

    def start(self):
        """Begin study session, looping through each card in the deck.
        User gets two attempts per card; tracks correct answers and displays summary.
        """
        self.correct = 0
        self.total = 0
        for card in self.deck.cards:
            card.display()
            first = input("Your answer: ")
            if card.check_answer(first):
                print("Correct! \n")
                self.correct += 1
                self.total += 1
            else:
                print("Incorrect. Please try again.")
                print("Answer Options:", ", ".join(card.get_options()) + "\n")
                second = input("The right answer pleaseeee: ")
                if card.check_answer(second):
                    print("Correct!\n")
                    self.correct += 1
                else:
                    print(f"Incorrect. The correct answer is {card.response}.\n")
                self.total += 1

        # After all q's, print summary
        print(f"Correct   : {self.correct}")
        print(f"Questions : {self.total}")
        print(f"Final Grade : {self.__str__()}")
