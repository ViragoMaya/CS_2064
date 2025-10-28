"""This module defines a Player class to be used in a Dice game."""


class Player:
    """Player object to simulate a turn using a Die object.

    Attributes:
        name (str): Player's name
        roll (int): Player's last roll
        score (int): Player's score
    """

    def __init__(self, name):
        """Initializes the Player object.

        Args:
            name (str): The name of the Player
        """
        self.name = name
        self.roll = None
        self.score = 0
        #parametr list nd above are defult values that will cahnge after

    def take_turn(self, die):
        """Simulates a Players turn by rolling the die and updating the score.

        Args:
            die (Die): a single die
        """
        self.roll = die.roll()
        print(f"{self.name} rolled a {self.roll}")
