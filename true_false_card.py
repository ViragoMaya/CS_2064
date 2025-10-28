"""Ghazal Tanavade
TrueFalseCard class for the Flashcard system.
"""

from multiple_choice_card import MultipleChoiceCard  #third one down


class TrueFalseCard(MultipleChoiceCard):
    """Subclass of MultipleChoiceCard for T/F questions.

    Attributes inherited:
        prompt (str): Question shown to the user.
        response (str): Correct answer label ('t' or 'f').
        choices (dict): Answer options, always {"t": "true", "f": "false"}.
    """

    def __init__(self, question, answer):
        """Initialize a TrueFalseCard.

        Args:
            question (str): True/false question.
            answer (str): Label of the correct answer ('t' or 'f').

        """
        choices = {"t": "true", "f": "false"}
        super().__init__(question, answer, choices)

