"""Ghazal Tanavade

Flashcard base class for the quiz system.
"""


class Flashcard:
    """Base class representing a flashcard with a question and answer.

    Attributes:
        prompt (str): The question shown to the user
        response (str): The correct answer to the question (prompt)

    """

    def __init__(self, question, answer):
        """Initialize/construct a flashcard with question and answer.

        Args:
            question (str): The question/prompt for the flashcard
            answer (str): The correct answer to the question

        """
        self.prompt = question
        self.response = answer

    #defines how an object of the class will be converted to a string.
    def __str__(self):
        """Return string representation of the flashcard.

        Returns:
            str: Answer in format "Answer: <response>"

        """
        return f"Answer: {self.response}"

    def check_answer(self, user_input):
        """Check if user's answer matches the correct answer (case-insensitive).

        Args:
            user_input (str): The user's input to check

        Returns:
            bool: True if answer is correct, False otherwise

        """
        #case insensitive comparison making it lower case
        return user_input.lower() == self.response.lower()

    def display(self):
        """Display the question to the user in following format:
        "Question: <prompt>"
        """
        print(f"Question: {self.prompt}")

    def get_options(self):
        """Get available options for this flashcard type.

        Returns:
            list: List containing (str) "Fill in the blank" for base flashcard

        """
        return ["Fill in the blank"]
