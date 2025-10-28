"""Ghazal Tanavade
MultipleChoiceCard class for the Flashcard quiz system.
"""

from flashcard import Flashcard


class MultipleChoiceCard(Flashcard):
    """Subclass of Flashcard for multiple choice questions.

    Attributes:
        prompt (str): The question shown to the user (inherited).
        response (str): The correct answer label (inherited).
        choices (dict): Dictionary mapping labels to answer options.

    """

    def __init__(self, question, answer, choices):
        """Initialize a MultipleChoiceCard.

        Args:
            question (str): The multiple choice question.
            answer (str): The label of the correct answer (e.g., 'a').
            choices (dict): A mapping of answer labels to the answer text,
                e.g., {'a': 'A', 'b': 'B', 'c': 'C'}.

        """
        # Call the parent class constructor (Flashcard)
        super().__init__(question, answer)
        # Saves dict of choices (all possible answers) to object
        self.choices = choices

    def display(self):
        """Display the question and all choices to the user."""
        super().display()
        for label, choice in self.choices.items():
            print(f"{label}: {choice}")

    def get_options(self):
        """Return a list of possible answer labels."""
        return list(self.choices.keys())
